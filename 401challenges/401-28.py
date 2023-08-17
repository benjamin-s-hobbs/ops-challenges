#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-28.py Event Logging Tool Part 3 of 3
# Author:                       Ben Hobbs
# Date of latest revision:      08/16/2023
# Purpose:                      Ops Challenge: Event Logging Tool Part 3 of 3
#                               In your Python tool:
#                               Use StreamHandler and FileHandler in your Python script.
#                               FileHandler should write to a local file.
#                               StreamHandler should output to the terminal.

# References:
# Demo code Class28
# Marco Vazquez 401-Class28 topic intro 
# 401-11.py (NetworkSecurityToolScapy1)
# Python Logging: Using Handlers- https://realpython.com/python-logging/#using-handlers

# Import Libraries:
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import FileHandler
from logging.handlers import StreamHandler
from scapy.all import sr1, TCP, ICMP, IP

# Declaration of variables (Global):
configlog = logging.basicConfig(filename="myscan.log", format="%(asctime)s:%levelname)s:%message)s", level=logging.INFO)


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
configlog
logging.info("Single ping packet sent")
# Declaration of functions:

# Create a rotating log for port scans
rotate_pscanlog = logging.getLogger("Rotating Log")
rotate_pscanlog.setLevel(logging.DEBUG)

# add a handler
rotate_pscanlog_handle = RotatingFileHandler("~/ops-challenges/401challengeshandlelogs.txt/", maxBytes=25, backupCount=4)

# Write a function to test our specified range of ports (for loop)
# Write a function to send a RST packet if 0x12 flag is received (to close the open connection)
def scan_ports():
    global configlog
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
logging.info("Scan has been completed")



# End (end of script)
