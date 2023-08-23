#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-32.py Signature-based Malware Detection Part 2 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      08/22/2023
# Purpose:                      Ops Challenge: Signature-based Malware Detection Part 2 of 3
#                               In Python, Continue developing your Python malware detection tool.
#                               Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
#                               For each file scanned within the scope of your search directory:
#                               Generate the file’s MD5 hash using Hashlib.
#                               Assign the MD5 hash to a variable.
#                               Print the variable to the screen along with a timestamp, file name, file size, and complete (not relative) file path.
#                               
#                               TIP: You may need to bring in additional Python modules to complete today’s objective.
#                               The script should be tested to execute successfully in Python3.


# References:
# Demo code Class32
# Marco Vazquez 401-Class32 topic intro 
# 
# 

# Import Libraries:
# import os.walk 
#import platform 
#import hashlib
#import time 
#import cryptography
# Declaration of variables (Global):

# Declaration of functions:

# Write a function to scan every file in every folder in the input user path and print the result (in Linux)
def malware_scanlx():
    # pass the function of the scan into a variable for later use
    deepfilescan_lx = input("What file would you like to scan? ")
    deepdirscan_lx = input("What directory would you like to scan? ")

    while True:
        print(deepfilescan_lx)
        print(deepdirscan_lx)

    # pass the hashing of a file into a variable to call

    # walk that hash variable on down using the deepscan

    # Make sure to timestamp it

# Write a function to scan every file in every folder and print the result (in Windows)
# Write a function to scan every file in every folder and print the result (in MacOS)
# Main (calling functions):




# End (end of script)