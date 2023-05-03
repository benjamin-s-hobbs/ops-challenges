#!/bin/bash

# Script Name:                  Ops Challenge: Class07
# Author:                       Ben Hobbs
# Date of latest revision:      05/2/2023
# Purpose:                      Write a script the uses lshw to display system information to the screen about the following components: Name of the computer, CPU, RAM, 
#                               Display Adapter, Network Adapter. Use grep to filter out irrelevant information for the lshw output. Add text to the output clearly 
#                               indicating which component (such as CPU, RAM, etc.) the script is returning information about, and runs as Root; you may execute the 
#                               shell script with sudo or as Root

# Declaration of variables
mycpu=*-cpu
myRAM=*-memory
mydisp=*-display
mynet=*-network
 
# Declaration of functions

sudo_var1 () {

 sudo lshw -C cpu | grep -v firmware | grep -v version: | grep -v capabilities: 
 sudo lshw -C memory  
 sudo lshw -C display | grep -v version:
 sudo lshw -C network
 
} 

# Main:                          

sudo_var1


# End