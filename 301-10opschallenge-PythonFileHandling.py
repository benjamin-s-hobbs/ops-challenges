#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 interpreter and execute the script with it

# Script Name:                  Ops Challenge: 301Class10opschallenge-PythonFileHandling.py
# Author:                       Ben Hobbs
# Date of latest revision:      06/13/2023
# Purpose:                      Using file handling commands, create a Python script that creates a new .txt file,
#                               appends three lines, prints to the screen the first line, then deletes the .txt file.


# Import Libraries
import os

# Declaration of variables
# How to declare a variable in python
#   greeting = "Welcome to Python!"
# How to call a variable
#   print(greeting)



# Declaration of functions

# Create a new file if it does not exist
f = open("demofile.txt", "w")

# How to open a file
f = open("demofile.txt")

# How to open a file and read it
f = open("demofile.txt", "r")
print(f.read())

# How to return the five first characters of a file
f = open("demofile.txt", "r")
print(f.read(5))

# Close a file when you're finished
f = open("demofile.txt", "r")
print(f.readline())

# Main:
                     



# End
