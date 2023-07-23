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


import datetime
import time 
import os 
import smtplib
from getpass import getpass

# Declaration of variables
up = "Host is active"
down = "Host is down"
now = datetime.datetime.now
last = 0
ping_result = 0
curr = time.time()
date_time = datetime.fromtimestamp(curr)
email = input("Enter your email: ")
password = getpass("Enter your password: ")
ip = input("What IP address would you like to monitor? ")




# Declaration of functions

#Function to handle the up alert - changes from down to up
def send_down_Alert():
    
#Start smtp session
#TLS for encryption
# Authentication to the email account
# Sending the email 
    smtplib.sendmail("bot@codefellows.com", email, message)
# Close the session
quit()


#Function to handle the down alert - changes from down to up 





# Function to handle the ping test
def ping_test():
    now = datetime.datetime.now()

    global ping_result
    global last

    # Ping result check - the logic that we fleshed out yesterday 
    if ((ping_result != last) and (ping_result == up)):

        # Change the value of last (because we just confirmed it was "up" in the previous line of code)
        last = up
        # Calling the function to send the email
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):

        # Change the value of last (because we just confirmed it was "down" in the previous line of code)
        last = down
        # Calling the function to send the email
        send_downAlert()

    # Do the actual ping (using a local variable called response)
    response = os.system("ping -i 2" + ip)

    # Evaluate the ping response
    if response == 0:
        ping_result = up
    else:
        ping_result = down
    print(str(now) + " " + str(ping) + " to " ip) 




#Print current date and time
now = datetime.now()
print("Current date and time: ")
print(str(now))
def test_ping(target):
    
    # Evaluate the response as either success or failure.
    
    print(ping_result)

while True:
    ping = os.system("ping target -i 2")
    print(ping)


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