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


# create a Python script that creates a new .txt file
f = open("testfile.txt", "w")

# appends three lines
intro = ["Hello World \n", "I'm new here \n", "I think I can do this though \n", "Look at me go World! \n"]

# Declaration of functions

# create a Python script that creates a new .txt file
open("testfile.txt", "w")
# appends three lines
with open("testfile.txt", "a") as file:
    file.write(intro)
# prints to the screen the first line
f = open("testfile.txt", "r")
print(f.read(12))
# then deletes the .txt file.
os.remove("testfile.txt")

# Main:

# create a Python script that creates a new .txt file
open("testfile.txt", "w")
# appends three lines
with open("testfile.txt", "a") as file:
    file.write(intro)
# prints to the screen the first line
f = open("testfile.txt", "r")
print(f.read(12))
# then deletes the .txt file.
os.remove("testfile.txt")                    



# End
