#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-18.py Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      08/2/2023
# Purpose:                      First, setup your target ZIP file.
#                               Create a .txt file containing a secret message.
#                               Follow the guide, How to Protect Zip file with Password, to archive the .txt 
#                               file with password protection.
#                               Next, add a new mode to your Python brute force tool that allows you to brute force 
#                               attack a password-locked zip file.
#                               Use the zipfile library.
#                               Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.

# References:
# Demo code Class18
# Marco Vazquez 401-Class18 topic intro 
# https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/
# 

# Import Libraries:
import sys
import os
import time
from getpass import getpass
import cryptography
import paramiko
import socket 
import termcolor
import zipfile 


# Declaration of variables (Global):
# Does your variable NEED to be global?


# Declaration of functions:

# Write a function to attack a password-locked .zip file
def attack_zip():
    # Identify where the file you want to open is 
    zip_lockd = input("What is the path to the .zip file that you'd like to open? \n")
    # Pass your rockme.txt wordlist (or variant) to a variable
    zipfile.ZipFile(zip_lockd, 'r')


# Write a function to add a new mode to our menu

# Write a function to accept input of a word list
#    def dict_iterator():
#        filepath = input("Enter your dictionary filepath:\n")
#        # Iterate through the word list
#        file = open(filepath, encoding = "ISO-8859-1")  # address encoding problem
#        # Assign the word being read to a variable
#        line = file.readline()
#        while line:
#            line = line.rstrip()
#            word = line
#            # Print the value of the variable to the screen.
#            print(word)
#            # Add a delay between words (1 sec)
#            time.sleep(1)
#            line = file.readline()
#        file.close()

# Write a function to accept input of a string

# Search the word list for the user input string.
# Print the result of the search to the screen.

def check_password():
    # Define a string to a variable
    usrpasswd = getpass("What password would you like to check? ")
    
    # Accept a user input word list file path
    filepath = input("Enter your dictionary filepath:\n")
#   # Check user input against the wordlist at "filepath" 
    print(f"checking your input password against the list in '{filepath}', just a moment...")

    file = open(filepath, 'r')
    line = file.readline()
    wordlist = []

    # While loop to add the password to the wordlist IF it isn't there already.
    while line:
        line = line.rstrip()
        # Adds the word to the wordlist variable which is an array
        wordlist.append(line)
        line = file.readline()
    file.close()

    if usrpasswd not in wordlist:
        print("Password accepted. Safety First...Thank you for your cooperation. Have a nice day.")
        strength = True
    elif usrpasswd in wordlist:
        print("Password unfit for system parameters. Attempt another password...Extreme Force Authorized in 20 seconds.")
        strength = False

        while strength is False:
            # Ask the user for a new password
            new_usrpasswd = getpass("Password is weak. Do. It. Again. >>> \n")

            if new_usrpasswd in wordlist: 
                print("TRY. AGAIN!!!")
            elif new_usrpasswd not in wordlist:
                print("Password Accepted")
                # Breaks the while loop
                strength = True

# Write a function to combine these options into a user menu
#def BForce_tool():
#    if __name__ == "__main__": # when my computer runs this file...do this stuff
        while True:
            # Call the first function "Mode 1: Offensive; Dictionary Iterator"
            # Call the second function "Mode 2: Defensive; Password Recognized"
            mode = input("""
#    Brute Force Wordlist Attack Tool Menu
#    1 - Offensive, Dictionary Iterator                         
#    2 - Defensive, Password Recognized
#    3 - Exit
#        Please enter a number: 
#    """)
            if (mode == "1"):
                dict_iterator()
            elif (mode == "2"):
                check_password()
            elif (mode == '3'):
                break
            else:
                print("Invalid selection...I'm sorry, you must be at least 18 years old or at least know how numbers work to use this tool")

# Main (call your functions)
attack_zip()
#BForce_tool()

# End (end of script)