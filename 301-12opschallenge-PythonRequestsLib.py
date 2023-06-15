#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 301Class12opschallenge-PythonRequestsLibrary.py
# Author:                       Ben Hobbs
# Date of latest revision:      06/14/2023
# Purpose:                      Create a Python script that performs the following:
#                               Prompts the user to type a string input as the variable for your destination URL.
#                               Prompts the user to select a HTTP Method of the following options:
#                                   GET
#                                   POST
#                                   PUT
#                                   DELETE
#                                   HEAD
#                                   PATCH
#                                   OPTIONS
#                               Prints to the screen the entire request your script is about to send. 
#                               Ask the user to confirm before proceeding.
#                               Using the requests library, performs a request against the destination URL with the 
#                               HTTP Method selected by the user. 
#                               For the given header, translate the codes into plain terms that print to the screen; 
#                               for example, a 404 error should print "Site not found" to the terminal instead of 404.
#                               For the given URL, print response header information to the screen.

# References:

# Import Libraries
# use this to import libraries in a virtual environment>>>  "python3 -m pip install <LIBRARY NAME> --upgrade"
import requests

# Declaration of variables
# How to declare a variable in python
#   greeting = "Welcome to Python!"
# How to call a variable
#   print(greeting)

gogetr = requests.get('https://api.github.com')
postr = requests.post('https://api.github.com')
gogetr = requests.put('https://api.github.com')
deleter = requests.delete('https://api.github.com')
headr = requests.head('https://api.github.com')
patchr = requests.patch('https://api.github.com')
optionsr = requests.options('https://api.github.com')


# Declaration of functions




# Main:

#  Prints to the screen the entire request your script is about to send. 

#  Ask the user to confirm before proceeding.

#  Using the requests library, performs a request against the destination URL with the 

#  HTTP Method selected by the user. 

#  For the given header, translate the codes into plain terms that print to the screen; 
#  for example, a 404 error should print "Site not found" to the terminal instead of 404.

#  For the given URL, print response header information to the screen.
                 

# End