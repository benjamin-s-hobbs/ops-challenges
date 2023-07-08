#!/bin/bash

# Script Name:                  Ops Challenge: 301Class05 Clearing Logs
# Author:                       Ben Hobbs
# Date of latest revision:      06/05/2023
# Purpose:                      To Write a bash script that performs the following tasks:
#                               Print to the screen the file size of the log files before compression
#                               Compress the contents of the log files listed below to a backup directory
#                               /var/log/syslog
#                               /var/log/wtmp
#                               The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#                               Example: /var/log/backups/syslog-20220928081457.zip
#                               Clear the contents of the log file
#                               Print to screen the file size of the compressed file
#                               Compare the size of the compressed files to the size of the original log files

# Declaration of variables

varlogfat1=(/var/log/syslog)
varlogfat2=(/var/log/wtmp)
varlogbk=(/var/log/backups/$varwhen)
varwhen=(date +"syslog-%Y%m%d%H%M%S")

# Declaration of functions

fade_away() {
 # Print to the screen the file size of the log files before compression
 ls -lh * $varlogfat1
 ls -lh * $varlogfat2

 # Compress the contents of the log files listed below to a backup directory
 # The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
 # Example: /var/log/backups/syslog-20220928081457.zip
 zip $varlogfat1 >> /$varlogbk
 zip $varlogfat2 >> /$varlogbk

 # Clear the contents of the log file
 truncate -s 0 /$varlogfat1
 truncate -s 0 /$varlogfat2

 # Print to screen the file size of the compressed file
 ls -lh * /$varlogbk
 
}

# Main

fade_away

# End
