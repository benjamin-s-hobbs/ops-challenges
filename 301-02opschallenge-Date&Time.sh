#!/bin/bash

# Script Name:                  Ops Challenge: 301Class02
# Author:                       Ben Hobbs
# Date of latest revision:      05/31/2023
# Purpose:                      Create a bash script that: 
#                               Copies /var/log/syslog to the current working directory
#                               Appends the current date and time to the filename


# Declaration of variables

now=(syslog_date +%Y%m%d-%H%M)

# Declaration of functions

save_syslog{

touch ~/syslog301/$now
cp var/log/syslog ~/cwd/syslog301/$now    
}

# Main: 

save_syslog

echo copied $now

# End