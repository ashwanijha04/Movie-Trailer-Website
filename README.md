# Udacity_movie_trailer_P1
This repository contains a simple Python Project which displays some movies and their trailers when clicked.

# Installation
Make sure you have python 2.7 installed in your computer.
To check if python is installed, you can use the following commands-  

**WINDOWS-** 
 1) Download Python from this [link](https://www.python.org/download/releases/2.7/)
 2) Install Python. [Helpful Link](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)
 
**MAC-**
 1) Check if you have python installed.
    Command: _python --version_
    If you get an output with the python version, skip the installation part.
 
 2) If Python is not installed, install Xcode from the App store.
 3) Go to step 1.
 4) Download Python from https://www.python.org/downloads/mac-osx/ and install it.
 5) Go to step 1.
 
**LINUX-**

First, install some dependencies:

sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
Then download using the following command:

version=2.7.13
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
Extract and go to the directory:

tar -xvf Python-$version.tgz
cd Python-$version
Now, install using the command you just tried, using checkinstall instead to make it easier to uninstall if needed:

_./configure
make
sudo checkinstall_
Change version to whichever version you need (version=2.7.1 or version=3.6.0, for example).

# USAGE
**MAC/LINUX:**
 1) Open a terminal and change directory to desktop using _cd Desktop_ command.
 2) Clone the repository using _git clone https://www.github.com/ashwanijha04/Udacity_movie_trailer_P1_
 3) Now change to the folder just cloned 'cd Udacity_movie_trailer_P1'.
 3) Type the following command - _python entertainment_center.py_
 4) Done!
 
 **WINDOWS:**
  1) Go to https://www.github.com/ashwanijha04/Udacity_movie_trailer_P1 and clone/download using the user interface provided.
  2) Extract the folder and open entertainment_center.py in the idle text editor provided by python.
  3) Run the module.
  4) Done
