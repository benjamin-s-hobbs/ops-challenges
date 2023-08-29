#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-36.py 
# Author:                       Ben Hobbs
# Date of latest revision:      08/28/2023
# Purpose:                      Ops Challenge: Web Application Fingerprinting
#                               For this lab you’ll need to develop and test your Python script from a Linux VM with the tools Nmap, Netcat, and Telnet installed. Generally speaking, Kali Linux is the recommendation for this challenge.
#                               In Python create a script that executes from a Linux box to perform the following:
#                               Prompts the user to type a URL or IP address.
#                               Prompts the user to type a port number.
#                               Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
#                               Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
#                               Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
.


# References:
# Demo code Class36
# Marco Vazquez 401-Class36 topic intro 
# 
# 

# Import Libraries:

import os
import system 
import time


# Declaration of variables (Global):


# Declaration of functions:

# Function to request user input



# Netcat function
def netcat_scan(addr, port):
    #os.system("nc " + addr + " " + port)
    
    # Create a socket and a connection
    #socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Telnet function
#def telnet_scan():
    #os.system("nc " + addr + " " + port)
    
    # Create a socket and a connection
    #socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Nmap function
#def nmap_scan():
# Menu Function (using the above three functions as options)
    #os.system("nc " + addr + " " + port)
    
    # Create a socket and a connection
    #socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Main (calling functions):




# End (end of script)