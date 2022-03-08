#!/bin/bash
cd Assignment1

# Get all java files in the Assignment1 directory
find . | grep -e "\.java" > all_java_files.txt

# Compile with JavaFX
javac --module-path /tmp/javafx-sdk-17.0.2/lib --add-modules javafx.fxml,javafx.controls -d . @all_java_files.txt 

# copy resource files (fxml) to the new compiled structure
cp src/main/resources/fsd/assignment/assignment1/main-view.fxml fsd/assignment/assignment1/
cp src/main/resources/fsd/assignment/assignment1/edit-students.fxml fsd/assignment/assignment1/
