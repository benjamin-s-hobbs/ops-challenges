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

# Import Libraries
from datetime import datetime
import os 

# Declaration of variables

#Print current date and time
now = datetime.now()
print("Current date and time: ")
print(str(now))

while True:
    ping = os.system("ping 8.8.8.8 -i 2")
    print(ping)
    print(str(now) + " " + str(ping) + " to 8.8.8.8")
# Declaration of functions
def test_ping(target):

    # Evaluate the response as either success or failure.
    if response == 0:
        pingstatus = "Host is active"
    else:
        pingstatus = "Host is down"

    return pingstatus     
                                   
# Main:

test_ping("8.8.8.8") 

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Assign success or failure to a status variable.
# Infinite While loop


# For every ICMP transmission attempted, print the status variable along with a 
# comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# End