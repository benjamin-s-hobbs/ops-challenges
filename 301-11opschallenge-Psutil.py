#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 301Class11opschallenge-Psutil.py
# Author:                       Ben Hobbs
# Date of latest revision:      06/13/2023
# Purpose:                      Create a Python script that fetches this information using Psutil:
#                               -Time spent by normal processes executing in user mode
#                               -Time spent by processes executing in kernel mode
#                               -Time when system was idle
#                               -Time spent by priority processes executing in user mode
#                               -Time spent waiting for I/O to complete.
#                               -Time spent for servicing hardware interrupts
#                               -Time spent for servicing software interrupts
#                               -Time spent by other operating systems running in a virtualized environment
#                               -Time spent running a virtual CPU for guest operating 
#                                systems under the control of the Linux kernel

# References:                   https://www.geeksforgeeks.org/psutil-module-in-python/

# Import Libraries: 
# use this to import libraries in a virtual environment>>>  "python3 -m pip install <LIBRARY NAME> --upgrade"

import psutil


# Declaration of variables:
#       How to declare a variable in python:
#           greeting = "Welcome to Python!"
#       How to call a variable:
#           print(greeting)




# Declaration of functions:


print(psutil.cpu_times())


# Main:

                 

# End