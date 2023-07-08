#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 interpreter and execute the script with it

# Script Name:                  Ops Challenge: 301Class07opschallenge-DirectoryCreation.py
# Author:                       Ben Hobbs
# Date of latest revision:      06/7/2023
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
#                               Script must ask the user for a file path and read a user input string into a variable.
#                               Script must use the os.walk() function from the os library.
#                               Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Import Libraries
import os

# Declaration of variables
# How to declare a variable in python
#   greeting = "Welcome to Python!"
# How to call a variable
#   print(greeting)
user_name = input("What is your name?")
userpath = input("What filepath would you like to see? ")
varpath = os.walk(userpath)

# Declaration of functions
def show_me_logs(user_name): 
 
 
 print("use " + userpath +", correct?")
 print(varpath)


# Main:
                     



# End
