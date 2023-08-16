#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-26.py Event Logging Tool Part 1 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      08/14/2023
# Purpose:                      First, visit Python Logging Tutorial and practice the Basic Logging Tutorial.
#                               Next, review terminology at What Are stdin, stdout, and stderr on Linux? 
#                               before visiting Logging Module in Python for some examples to get you started.
#                               By now, you will have created several Python scripts in your public repo. 
#                               Select one of your Python tools created during this class so far that does not have a logging feature. 
#                               On that tool:
#                               Add logging capabilities to your Python tool using the logging library.
#                               Experiment with log types. Build in some error handling, then induce some errors. 
#                               Send log data to a file in the local directory.
#                               Confirm your logging feature is working as expected.

# References:
# Demo code Class26
# Marco Vazquez 401-Class26 topic intro 
# Marco Vazquez 401-Class27 topic review 
# 401-11.py (NetworkSecurityToolScapy1)
#
# Import Libraries:
import logging
from scapy.all import sr1, TCP, ICMP, IP



# Declaration of variables (Global):

# Define target host and port to scan

# Set the network range using variable.
network_cidr = "xxx.xxx.xxx.xxx/xx"

host = "scanme.namp.org"
port_range = 22
scr_port = 22
dst_port = 22

# Create an ARP packet using ARP() method.
# arp_pack = ans, unans = srp(IP(dst=host)/ARP(dport=dst_port), timeout=2)

# Create an Ethernet packet using Ether() method.

# Set the destination to broadcast using variable hwdst.
# Combine ARP request packet and Ethernet frame using ‘/’.

# TCP ping packet
response= sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
print(response)

# sends a single ping and prints out the response packet
p = sr1(IP(dst=host)/ICMP())
if p:
    p.show()
# 401-26: Create a log showing a single ping was sent.
logging.basicConfig(filename="myscan.log", format="%(asctime)s:%levelname)s:%message)s", level=logging.INFO)
logging.info("Single ping packet sent")
# Declaration of functions:

# Write a function to test our specified range of ports (for loop)
# Write a function to send a RST packet if 0x12 flag is received (to close the open connection)
def scan_ports():
    logging.basicConfig(filename="myscan.log", format="%(asctime)s:%levelname)s:%message)s", level=logging.INFO)
    # 401-26: Create a log that port scanning of xxx.xxx.xxx.xxx/xx has begun
    logging.info("port scan initiated on " + network_cidr)
    if (response.haslayer(TCP)):
        #Gets the value of the flag in the TCP packet. Compares it to 0x12 (SYN-ACK)
        if (response.getlayer(TCP).flags == 0x12):
            # Then the port is open. Send a RST packet to close it.
            send_rst = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
            send_rst
            # 401-26: Create a log to show RST packet was sent to close open port
            logging.info("RST packet sent to close open port")
            # Notify the user that the port is open.
            print(f"{host}:{dst_port} is open.")
            print(host + str(dst_port) + " is open.")
        # Gets the value of the flag in the TCP packet. Compares it to 0x14 (RST)
        elif (response.getlayer(TCP).flags == 0x14):
            # Then the port is closed. Notify user the port is closed.
            print(f"{host}:{dst_port} is closed.")
            print(host + str(dst_port) + " is closed.")
            # 401-26: Create a log to show that scan determined port is closed.
            logging.info("port closed")
        # Gets the value of the flag in the TCP packet. No flag in the TCP packet?
        else:
            # if no flag is received, notify the user the port is filtered and silently dropped.
            print(f"{host}:{dst_port} is filtered and silently dropped.")
            print(host + str(dst_port) + " is filtered and silently dropped.")
            # 401-26: Create a log to show that the port is filtered and silently dropped
            logging.info("port filtered and dropped silently")


# Main (calling functions):

scan_ports()
# 401-26: Create a log to show that the port scan is complete.
logging.basicConfig(filename="myscan.log", format="%(asctime)s:%levelname)s:%message)s", level=logging.INFO)
logging.info("Scan has been completed")



# End (end of script)