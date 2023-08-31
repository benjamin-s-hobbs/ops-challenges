#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-31.py Signature-based Malware Detection Part 1 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      08/21/2023
# Purpose:                      Ops Challenge: Signature-based Malware Detection Part 1 of 3
#                               In Python, write a script that will:
#                               
#                               Prompt the user to type in a file name to search for.
#                               Prompt the user for a directory to search in.
#                               Search each file in the directory by name.
#                               
#                               TIP: You may need to perform different commands depending on what OS you’re executing the script on.
#                               
#                               For each positive detection, print to the screen the file name and location.
#                               At the end of the search process, print to the screen how many files were searched and how many hits were found.
#                               The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.


# References:
# Demo code Class31
# Marco Vazquez 401-Class31 topic intro 
# Marco Vazquez 401-Class32 topic review
# 

# Import Libraries:
import os
import time
import platform

# Declaration of variables (Global):

# Declaration of functions:

# Write a function to search each file in an identified directory (for Linux)
def linux_Search():
# Get user input for a filename to search
# Get user input for a directory to search
    what_lxfile = input("What file are you looking for? ")
    what_lxdir = input("What directory are you looking for? ")

    


# Write a function to search each file in an identified directory (for Windows)
# Write a function to search each file in an identified directory (for MacOS)

# Main (calling functions):

linux_Search()


# End (end of script)