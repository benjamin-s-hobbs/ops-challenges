# Script Name:                  Ops Challenge: Class12 (psgrep.ps.1)
# Author:                       Ben Hobbs
# Date of latest revision:      05/09/2023
# Purpose:                      Write a Powershell script that returns the IPv4 address of the computer, using Select-String cmdlet 
#                               to only return the IPv4 address string and no other extraneous information.

# Declaration of variables
var1=IPv4
# Declaration of functions

# Main:                

# Remember to follow this class’s commenting requirements on all scripts.

# Create a Powershell script that performs the following operations:
# For this challenge, you must use at least one variable and one function.

# Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
ipconfig /all | Out-File C:\Users\Ben142\Desktop\network_report.txt

# Use Select-String to search network_report.txt and return only the IP version 4 address.
Select-String -Pattern 'var1' -Path 'C:\Users\Ben142\Desktop\network_report.txt'

# Remove the network_report.txt when you are finished searching it.
Remove-Item -Path 'C:\Users\Ben142\Desktop\network_report.txt'


# End