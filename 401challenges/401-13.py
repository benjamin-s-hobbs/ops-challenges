#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-13-NetworkSecurityToolScapy3.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/26/2023
# Purpose:                      The final iteration of your network scanning tool will perform the following:
#                                    Ping an IP address determined by the user.
#                                    If the host exists, scan its ports and determine if any are open.
#                                    In Python, combine the two modes (port and ping) of your network scanner script.
#                                    Eliminate the choice of mode selection.
#                                    Continue to prompt the user for an IP address to target.
#                                    Move port scan to its own function.
#                                    Call the port scan function if the host is responsive to ICMP echo requests.
#                                    Print the output to the screen.

# References:
# Demo code
# Marco Vasquez 401-Class13 topic intro 
# 

# Import Libraries:
import sys
import ipaddress 
import time
from scapy.all import sr1, TCP, ICMP, IP



# Declaration of variables (Global):

# Set the network range using variable.
network_cidr = ()
ip_list = ipaddress.IPv4Network(network_cidr)
for ip in ip_list:
    print(ip)
host = ip        
host_count = 0
port_range = len("") 
scr_port = 22
dst_port = 22

# TCP packet
response= sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
print(response)
# ICMP ping packet 
response = sr1(IP(dst=str(host))/ICMP(),timeout=1, verbose=0)
print(response)


# Declaration of functions:

# Write a function to test our specified range of ports (for loop)
# Write a function to send a RST packet if 0x12 flag is received (to close the open connection)
def scan_ports():
    if (response.haslayer(TCP)):
        # Gets the value of the flag in the TCP packet. Compares it to 0x12 (SYN-ACK)
        if (response.getlayer(TCP).flags == 0x12):
            # Then the port is open. Send a RST packet to close it.
            send_rst = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
            print(send_rst)
            # Notify the user that the port is open.
            print(f"{host}:{dst_port} is open.")
            
            # Gets the value of the flag in the TCP packet. Compares it to 0x14 (RST)
        elif (response.getlayer(TCP).flags == 0x14):
            # Then the port is closed. Notify user the port is closed.
            print(f"{host}:{dst_port} is closed.")
            # Gets the value of the flag in the TCP packet. No flag in the TCP packet?
        else:
            # if no flag is received, notify the user the port is filtered and siliently dropped.
            print(f"{host}:{dst_port} is filtered and silently dropped.")
            

# Write a function to conduct ICMP ping and scan
def ping_scan():
    global network_cidr
    global ip_list
    global host_count
    # Prompt user for input. Ask for network to scan (in CIDR format)
    network_cidr = input(" What network (in CIDR format) do you want to sweep? ")
    # Display the network the user entered to be swept.
    print(network_cidr)
    # Begin ICMP ping sweep for each host on the network
    for host in ip_list:
    # Include an exception for the network ID address (first) and the broadcast address (last)
        if (host in (ip_list.network_address, ip_list.broadcast_address)):
        # Skip them
            continue
        # Send ICMP packet and puts it into variable 'response.' Print 'response'. 
        
        # If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the
        # host is actively blocking ICMP traffic.
            response = sr1(IP(dst=str(host))/ICMP(),timeout=1, verbose=0)
            print(response)
        elif (int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13] ):
            
            print("host is blocking traffic")
            print(host_count)
    # Otherwise, inform the user that the host is responding.
        else:
            print("host is responding")
            host_count += 1
            print(host_count)
            scan_ports()
            print("total hosts responding " + str(host_count))




    # Write a function to create a user menu. 1) TCP scan, 2) ICMP ping sweep
#    def select_scan():
#        scan = input("\nWhat would you like to do? Please choose an option. \n 1) - TCP Scan \n 2) - ICMP ping sweep  \n Please enter a number: ")
#        if (scan == "1"):
#            scan_ports()
#            print("Now conducting TCP scan.")
#       elif (scan == "2"):
#            ping_sweep()
#            print("Now conducting ICMP ping sweep.")
#        elif (scan == "3"):
#            sys.exit
#        else:
#            print("Invalid Selection, self-destruct sequence activated...")
#            time.sleep(2)
#            print("3")
#            time.sleep(2)
#            print("2")
#            time.sleep(2)
#            print("1")
#            time.sleep(2)
#            print("goodbye")

# Main (calling functions):

#    select_scan()

ping_scan()

# End (end of script)