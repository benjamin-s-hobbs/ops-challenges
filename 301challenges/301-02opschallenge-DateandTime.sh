#!/bin/bash

# Script Name:                  Ops Challenge: 301Class02
# Author:                       Ben Hobbs
# Date of latest revision:      05/31/2023
# Purpose:                      Create a bash script that: 
#                               Copies /var/log/syslog to the current working directory
#                               Appends the current date and time to the filename


# Declaration of variables

now=$(date +%Y%m%d-%H%M)
filenow=(syslog_$now)

# Declaration of functions

save_syslog() {

mkdir ~/syslog301
touch ~/syslog301/$filenow

cp /var/log/syslog ~/syslog301/$filenow 

echo copied syslog to $filenow at $now

}

# Main: 

save_syslog



# End