#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-12-NetworkSecurityToolScapy2.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/25/2023
# Purpose:                      In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
#                               Utilize the scapy library
#                               Define host IP
#                               Define port range or specific set of ports to scan
#                               Test each port in the specified range using a for loop
#                               If flag 0x12 received, send a RST packet to graciously close the open connection. 
#                               Notify the user the port is open.
#                               If flag 0x14 received, notify user the port is closed.
#                               If no flag is received, notify the user the port is filtered and silently dropped.


# References:
# Demo code
# Marco Vasquez 401-Class12 topic intro 
# https://scapy.readthedocs.io/en/latest/usage.html

# Import Libraries:
import sys
import ipaddress 
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
#    p=sr1(IP(dst=host)/ICMP())
#    if p:
#        p.show()

# Declaration of functions:

# Write a function to test our specified range of ports (for loop)
# Write a function to send a RST packet if 0x12 flag is received (to close the open connection)
def scan_ports():
    if (response.haslayer(TCP)):
        #Gets the value of the flag in the TCP packet. Compares it to 0x12 (SYN-ACK)
        if (response.getlayer(TCP).flags == 0x12):
            # Then the port is open. Send a RST packet to close it.
            send_rst = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
            # Notify the user that the port is open.
            print(f"{host}:{dst_port} is open.")
            print(host + str(dst_port) + " is open.")
        # Gets the value of the flag in the TCP packet. Compares it to 0x14 (RST)
        elif (response.getlayer(TCP).flags == 0x14):
            # Then the port is closed. Notify user the port is closed.
            print(f"{host}:{dst_port} is closed.")
            print(host + str(dst_port) + " is closed.")
        # Gets the value of the flag in the TCP packet. No flag in the TCP packet?
        else:
            # if no flag is received, notify the user the port is filtered and siliently dropped.
            print(f"{host}:{dst_port} is filtered and silently dropped.")
            print(host + str(dst_port) + " is filtered and silently dropped.")


# Main (calling functions):

scan_ports()



# End (end of script)