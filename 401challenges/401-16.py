#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-16.py Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      07/31/2023
# Purpose:                      In Python, create a script that prompts the user to select one of the following modes:
#                               Mode 1: Offensive; Dictionary Iterator
#                               Accepts a user input word list file path and iterates through the word list, 
#                               assigning the word being read to a variable.
#                               Add a delay between words.
#                               Print to the screen the value of the variable.
#                               Mode 2: Defensive; Password Recognized
#                               Accepts a user input string.
#                               Accepts a user input word list file path.
#                               Search the word list for the user input string.
#                               Print to the screen whether the string appeared in the word list.


# References:
# Demo code Class16
# Marco Vasquez 401-Class16 topic intro 
# 

# Import Libraries:
import os
import time
import getpass


# Declaration of variables (Global):
# Does your variable NEED to be global?


# Declaration of functions:

# Write a function to accept input of a word list
def dict_iterator():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    # Iterate through the word list
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    # Assign the word being read to a variable
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        # Print the value of the variable to the screen.
        print(word)
        # Add a delay between words (1 sec)
        time.sleep(1)
        line = file.readline()
    file.close()

# Write a function to accept input of a string

# Search the word list for the user input string.
# Print the result of the search to the screen.
def check_password():
    # Define a string to a variable
    password= input("What password would you like to check?\n")
    # Accept a user input word list file path
    filepath = input("Enter your dictionary filepath:\n")
    search = 
    print(search)

# Write a function to combine these options into a user menu
def BForce_tool():
    if __name__ == "__main__": # when my computer runs this file...do this stuff
        while True:
            # Call the first function "Mode 1: Offensive; Dictionary Iterator"
            # Call the second function "Mode 2: Defensive; Password Recognized"
            mode = input("""
    Brute Force Wordlist Attack Tool Menu
    1 - Offensive, Dictionary Iterator                         
    2 - Defensive, Password Recognized
    3 - Exit
        Please enter a number: 
    """)
            if (mode == "1"):
                dict_iterator()
            elif (mode == "2"):
                check_password()
            elif (mode == '3'):
                break
            else:
                print("Invalid selection...I'm sorry, you must be at least 18 years old or at least know how numbers work to use this tool")

# Main (call your functions)

BForce_tool()

# End (end of script)