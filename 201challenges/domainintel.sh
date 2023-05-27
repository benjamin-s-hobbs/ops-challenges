#!/bin/bash

# Script Name:                  Ops Challenge: Class13 (domainintel.sh)
# Author:                       Ben Hobbs
# Date of latest revision:      05/10/2023
# Purpose:                      Create a script that asks a user to type a domain, then displays information about the typed domain. 
#                               Operations that must be used include: whois, dig, host, nslookup

# Declaration of variables
# Take a user input string. Presumably the string is a domain name such as Google.com.
string1="www.google.com"

# Declaration of functions
print_OSINT () {

#Run whois against a user input string.
whois $string1 >> ~/ops-201d8-code-challenges/OSINT1.txt

#Run dig against the user input string.
dig $string1 >> ~ops-201d8-code-challenges/OSINT1.txt

#Run host against the user input string.
host $string1 >> ~/ops-201d8-code-challenges/OSINT1.txt

#Run nslookup against the user input string.
nslookup $string1 >> ~/ops-201d8-code-challenges/OSINT1.txt

}

# Main:                          

print_OSINT

# End