#!/usr/bin/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-42.py 
# Author:                       Ben Hobbs
# Date of latest revision:      09/7/2023
# Purpose:                      Ops Challenge: Attack Tools Part 2 of 3
#                               Finish DEMO.md in your class repo> Class 42 > Challenges folder



# References:
# Demo code Class42
# Marco Vazquez 401-Class42 topic intro 
# Marco Vazquez 401-Class43 topic review 

# Import Libraries:

import nmap

# Declaration of variables (Global):

# Declaration of functions:

def tool_autonmap():

    scanner = nmap.PortScanner()

    print("Nmap Automation Tool")
    print("--------------------")

    ip_addr = input("IP address to scan: ")
    print("The IP you entered is: ", ip_addr)
    type(ip_addr)

    resp = input("""\nSelect scan to execute:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) ARP Scan             \n""")
    print("You have selected option: ", resp)

    range = input("Enter a range of ports that you want to scan; ex: 1-50: ")

    if resp == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -sU -Su')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -PR -A')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    else resp >= '4':
        print("Please enter a valid option")
        print("non-valid response entered")
        print("starting self-destruct sequence... ")

# Main (calling functions):

tool_autonmap()

# End(end of script):