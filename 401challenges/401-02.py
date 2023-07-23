#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-02opschallenge-UptimeSensor1.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/11/2023
# Purpose:                      In Python, create an uptime sensor tool that uses ICMP packets to evaluate if 
#                               hosts on the LAN are up or down.
#                               

# References:
# https://realpython.com/python-datetime/#using-the-python-datetime-module 
# Marco Vasquez in-class reference

# Import Libraries
from datetime import datetime
import os 
import time

# Declaration of variables (global):



# Declaration of functions:

# Write a function to send a test ping to a target.
# 
def test_ping(target):
    response = os.system("ping -c 1 " + target)
    # Evaluate the response as either success or failure.
    if response == 0:
        pingstatus = " Host is active at "
    else:
        pingstatus = " Host is down at "
    # Assign success or failure to a status variable.
    return pingstatus
    # Handle the function output

# Create an input to pass to a variable for a target IP address
target = input("What IP address would you like to target? ")
pingstatus = test_ping(target)
# Infinite While loop
# Infinite loop to create a heartbeat sensor
while True:
    #Print current date and time
    now = datetime.now()
    # For every ICMP transmission attempted, print the status variable along with a 
    # comprehensive timestamp and destination IP tested.
    # Example output: 2020-10-05 17:57:57.510261 Host is active at 8.8.8.8
    print(str(now) + pingstatus + target)
    # Transmit a single ICMP (ping) packet to a specific IP every two seconds.
    time.sleep(2)

# Main:

test_ping(target)


# End