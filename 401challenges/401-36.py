#!/usr/bin/python3
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



# References:
# Demo code Class36
# Marco Vazquez 401-Class36 topic intro 
# https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
# # Marco Vazquez 401-Class37 topic review 

# Import Libraries:

import os
import system
import time
import socket

# Declaration of variables (Global):

# Create variables from user input 
# Target URL or IP address
user_target = input("What URL or IP address would you like to target? ")
# Target port
port_target = input("What port would you like to target? ")

# Declaration of functions:

# Netcat function to perform banner grabbing 
def netcat_scan(address, port):
    global user_target
    global port_target

    user_target = address
    port_target = port

    os.system("nc " + address + " " + port)
    
    # Create a socket and a connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((address), int(port))
# Telnet function
def telnet_scan(address, port):
    global user_target
    global port_target

    user_target = address
    port_target = port

    os.system("telnet " + address + " " + port)
    
    # Create a socket and a connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((address), int(port))
# Nmap function
def nmap_scan(address, port):
    global user_target
    global port_target

    user_target = address
    port_target = port

    # Create a socket and a connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((address, int(port)))
    
    run = os.system("nmap " + "-sV" + "-p"+ port + " " + address)
    
    socket1.sendall(run.encode())
    socket1.close

# Menu Function (using the above three functions as options)
def menu_bgrabber():
    global user_target
    global port_target

    bgrabber = input("\nWhat would you like to do? Please choose an option. \n 1) - Netcat Banner Grab \n 2) - Telnet Banner Grab  \n 3) - Nmap Banner Grab \n 4) - Exit \n Please enter a number: ")
    if (bgrabber == "1"):
        netcat_scan(address, port)
        print("Now conducting netcat banner grab.")
    elif (bgrabber == "2"):
        telnet_scan(address, port)
        print("Now conducting telnet banner grab.")
    elif (bgrabber == "3"):
        nmap_scan(address, port)
        print("Now conducting nmap banner grab.")
    elif (bgrabber == "4"):
        sys.exit
    else:
        print("Invalid Selection, self-destruct sequence activated...")
        time.sleep(2)
        print("3")
        time.sleep(2)
        print("2")
        time.sleep(2)
        print("1")
        time.sleep(2)
        print("goodbye")

# Main (calling functions):

menu_bgrabber():


# End(end of script):