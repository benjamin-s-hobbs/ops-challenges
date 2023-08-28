#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-36.py 
# Author:                       Ben Hobbs
# Date of latest revision:      08/28/2023
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
# Raven (TA)
# 

# Import Libraries:

import os
import system 
import time


# Declaration of variables (Global):


# Declaration of functions:

# Netcat function
def netcat_scan(addr, port):
    #os.system("nc " + addr + " " + port)
    
    # Create a socket and a connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Main (calling functions):




# End (end of script)