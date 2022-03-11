import sys, glob, subprocess, re
import os
import termcolor

def marking_error(s):
    termcolor.cprint("ERROR :: " + s, 'red')
    print("Stopping marking process")
    # attempt to remove any Assignment1 directories
    sp_ret = subprocess.run(["rm", "-rf", "Assignment1"])
    exit()

print_success = lambda x: termcolor.cprint(x, 'green')

def load_file(fname):
    with open(fname, "r") as f:
        file = f.readlines()
    return file

print("=== Starting marking ===")

# Check for a zip file to mark
assignment_zip = glob.glob("*.zip")

if assignment_zip == []:
    marking_error("No assignment file found...\nPlease add a zip file to the current directory for marking")

print_success("Assignment zip file present")
assignment_zip = assignment_zip[0]

# Check the naming convention
student_id = re.findall(r'_\d{7}', assignment_zip)

if student_id == []:
    marking_error("Failed to extract student ID please include this in your assignment zip file name")

student_id = student_id[0].replace("_", "")
print_success("Student ID: {} extracted".format(student_id))

# Extract student assignment
    
sp_ret = subprocess.run(["7z", "x", assignment_zip])
if sp_ret.returncode != 0:
    marking_error("Extraction failed!")

print_success("Zip file extraction successful")

# Check for file named 'Assignment1'
if not(os.path.exists("Assignment1") and os.path.exists("Assignment1/src")):
    marking_error("Assignment1 or Assignment1/src directories do not exist - Please review your submission file structure!")

print_success("Required directories (Assignment1 and Assignment1/src) exist")

# Convert DOS line endings to unix
sp_ret = subprocess.run(["dos2unix", "java_compile.sh"], capture_output=True)
if sp_ret.returncode < 0:
    print("Error in dos2unix conversion - this is not a problem if the rest of the code executes!\n{}".format(sp_ret.stderr))

# Compile and run java script (note: not javascript)
sp_ret = subprocess.run(["sh", "java_compile.sh"], capture_output=True)
if sp_ret.returncode < 0:
    marking_error("Execution of java_compile.sh failed - {}".format(sp_ret.stderr))

print_success("Execution of java_compile.sh succeeded")
if sp_ret.stderr.decode('ascii') == "":
    print_success("No compile errors")
else:
    marking_error("Compile errors:\n{}".format(sp_ret.stderr.decode('ascii')))

# Remove Assignment1 directory after all tests are done
sp_ret = subprocess.run(["rm", "-rf", "Assignment1"])
if sp_ret.returncode != 0:
    marking_error("Removal of Assignment1 directory failed")

print_success("Assignment1 directory successfully removed")
print_success("=== Marking complete ===")
