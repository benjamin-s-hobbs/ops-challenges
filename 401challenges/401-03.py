#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-03opschallenge-UptimeSensor2.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/12/2023
# Purpose:                      In Python, add the below features to your uptime sensor tool.
#                               The script must:

#                               Ask the user for an email address and password to use for sending notifications.
#                               Send an email to the administrator if a host status changes 
#                               (from “up” to “down” or “down” to “up”).
#                               Clearly indicate in the message which host status changed, 
#                               the status before and after, and a timestamp of the event.
#                               Important Notes
#                               DO NOT commit your email password in plain text within your script to GitHub 
#                               as this easily becomes public.
#                               Create a new “burner” account for this exercise. Do not use an existing email account.
#                               

# References: https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
# Marco Vasquez in-class reference (for resubmission)



# Import Libraries:
from datetime import datetime
import time 
import os 
import smtplib
from getpass import getpass

# Declaration of variables
up = " Host is active at "
down = " Host is down at "
last = 0
ping_result = 0

email = input("Enter your email: ")
password = getpass("Enter your password: ")
target = input("What IP address would you like to target? ")


# Declaration of functions

#Function to handle the up alert - changes from down to up
def send_upAlert():
    now = datetime.now

    #Start smtp session
    s = smtplib.SMTP("smtp.gmail.com", 587)
    
    #TLS for encryption
    s.starttls()
    # Authentication to the email account
    s.login(email, password)
    
    message = "YOUR SERVER IS BACK UP ON THE NETWORK!"

    #Sending the email 
    s.sendmail("bot@codefellows.com", email, message)
    
    # Close the session
    s.quit()


#Function to handle the down alert - changes from up to down 
def send_downAlert():
    now = datetime.now

    #Start smtp session
    s = smtplib.SMTP("smtp.gmail.com", 587)
    
    #TLS for encryption
    s.starttls()
    # Authentication to the email account
    s.login(email, password)

    message = "YOUR SERVER IS DOWN ON THE NETWORK- GO FIND THE PROBLEM!"

    #Sending the email 
    s.sendmail("bot@codefellows.com", email, message)
    
    # Close the session
    s.quit()

# Function to handle the ping test
def ping_test():
    now = datetime.now()

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
    response = os.system("ping -c 1" + target)

    # Evaluate the ping response
    if response == 0:
        ping_result = up
    else:
        ping_result = down
    print(now)
    print(target)

    #Main:
    # Infinite heartbeat
    while True:
        ping_test()
        time.sleep(2)

