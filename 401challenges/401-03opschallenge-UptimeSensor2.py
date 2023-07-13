#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-03opschallenge-UptimeSensor2.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/12/2023
# Purpose:                      In Python, create an uptime sensor tool that uses ICMP packets to evaluate if 
#                               hosts on the LAN are up or down.
#                               

# References:


# Import Libraries
from datetime import datetime
import os 
import smtplib
import getpass

# Declaration of variables

#Print current date and time
now = datetime.now()
print("Current date and time: ")
print(str(now))



# Declaration of functions
def test_ping(target):
    response = os.system("ping -i 2" + target)
    # Evaluate the response as either success or failure.
    if response == 0:
        pingstatus = "Host is active"
    else:
        pingstatus = "Host is down"
    print(pingstatus)

while True:
    ping = os.system("ping target -i 2")
    print(ping)
    print(str(now) + " " + str(ping) + " to target")        

# Main:

test_ping(target):

while True:
    test_ping("8.8.8.8") 

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Assign success or failure to a status variable.
# Infinite While loop


# For every ICMP transmission attempted, print the status variable along with a 
# comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# End