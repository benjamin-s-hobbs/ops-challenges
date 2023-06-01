#!/bin/bash

# Script Name:                  Ops Challenge: 301Class02
# Author:                       Ben Hobbs
# Date of latest revision:      05/31/2023
# Purpose:                      Create a bash script that: 
#                               Copies /var/log/syslog to the current working directory
#                               Appends the current date and time to the filename


# Declaration of variables

now=$()

# Declaration of functions

save_syslog{

cp var/log/syslog ~/cwd/syslog_now    
}

# Main: 

save_syslog

echo copied syslog_

# End