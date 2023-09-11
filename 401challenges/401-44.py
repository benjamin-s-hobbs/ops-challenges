#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-44.py Create a Port Scanner
# Author:                       Ben Hobbs
# Date of latest revision:      09/10/2023
# Purpose:                      Ops Challenge: Create a Port Scanner
#                               I


# References:
# Demo code Class44
# Socket Documentation: https://docs.python.org/3/library/socket.html
# 

# Import Libraries:
import socket

# Declaration of variables (Global):
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10
sockmod.settimeout(timeout)

hostip = input("What host IP would you like to use? ")
portnum = input("What port number would you like to use? ")# TODO: Collect a port number from the user
        # then convert it to an integer data type.
portno = int(portnum)
print(portno)


# Declaration of functions:

def portScanner(portno):
    if sockmod.connect((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call
        print("Port closed")
    else:
        print("Port open")

# Main (call your functions)
portScanner(port)


# End (end of script)