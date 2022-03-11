# FSAD Docker

Docker containers are a really useful way to *'containerise'* code, that is, we can create environments where users can execute a program without having to worry about code dependencies (all dependencies are included in the container). We can think of a container as a really lightweight virtual machine. If you're interested in dockerising everything on your computer see: [Jess Frazelle's dockerfiles](https://github.com/jessfraz/dockerfiles).

In FSAD we will use docker containers to allow you to test your code on *"our machines"* before you submit your assignment. For some assignments we will include some basic tests, for others we will just check your code will compile. Please take note that **just because you pass the early tests it does not mean you will pass the final tests**. To make sure you're covering all the marking criteria please read the assignment document carefully!

Below are setup instructions for various different operating systems.

### Using this repository

There are two options! Either download a zip file containing all the code (click the green code button), or [install git](https://github.com/git-guides/install-git) (make sure to place it on your computer, not a network drive like OneDrive), then in navigate to a location to store the code and (in terminal/comamnd line) type `git clone https://github.com/dfenth/fsad-docker.git`. The advantage of using git is that if we make any updates to the code, you can just type `git pull` to update the code. If you download the zip file, you'll need to re-download for each update.

### Windows Setup

---

Go to: [Get Docker](https://docs.docker.com/get-docker/) and follow the download instructions, specifically make sure virtualisation is enabled (it should tell you if virtualisation is enabled in the task manager (where you view CPU performance etc.)). If virtualisation isn't enabled there should be an option in the computer BIOS (lots of support is available from the internet for this).

Please note that we expect that you have installed Docker to `C:\Program Files`. If you have not then a small change needs to be made to the `run_marking.bat` script (detailed later).

If all else fails, you can download a [virtual machine](https://www.virtualbox.org/) along with a linux OS of your choice and follow the linux install guide.

### Mac Setup

---

With macos you have a few options!

#### Option 1: GUI

You can download the GUI application using: [Get Docker](https://docs.docker.com/get-docker/) (be careful of the achitecture).

#### Option 2: Brew

If you use the Brew package manager you can install docker with the command:

```bash
brew install --cask docker
```

### Linux Setup

---

With linux you have a few options!

#### Option 1: Official Way

Follow the instruction at [Install Docker Engine](https://docs.docker.com/engine/install/).

#### Option 2: Package Manager

If you use any kind of package manager you can install docker with the command (replacing `apt-get` with your particular package manager):

```bash
sudo apt-get update
sudo apt-get install docker.io
```

> Note: The package name of `docker` could be vary.

#### Option 3: Snap

If you use snap, the following command will help:

```bash
sudo snap install docker
```

### Running the container

---

Navigate to the appropriate folder for the assignment and place your zip file (named as specified in the assignment document) in the `Test` folder and open the directory in the terminal/command line (the directory which contains `Test`) then:

**Linux/macOS:**

```bash
sudo sh run_marking.sh
```

**Windows:**

If you installed docker to `C:\Program Files` you're good to go, just use the commands below. If you didn't then the first line of the batch script:

```batch
start "C:\Program Files\Docker\Docker\Docker Desktop.exe"
```

Needs to be changed:

```batch
start "<your-path-to-docker>\Docker\Docker Desktop.exe"
```

That's all!

Using command line:

```powershell
call run_marking.bat
```

Or using powershell:

```powershell
.\run_marking.bat
```
> Note: This may take a while the first time, but then should be much faster afterwards!
