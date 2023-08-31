#!/usr/bin/ python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-37.py Cookie Capture Capades
# Author:                       Ben Hobbs
# Date of latest revision:      08/29/2023
# Purpose:                      Ops Challenge: Cookie Capture Capades
#                               Copy the demo script for today as your template for this challenge.
#                               Complete the objectives listed at the bottom of the demo script.

# References:
# Demo code Class37
# Marco Vazquez 401-Class37 topic intro 
# https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/ 
# https://requests.readthedocs.io/en/latest/

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

# Import Libraries:
import requests


# Declaration of variables (Global):
# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

# Declaration of functions:

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
def good_monster():
    put = requests.put(targetsite, cookie)
    print(put)

# - Generate a .html file to capture the contents of the HTTP response
def give_jar():
    
# - Open it with Firefox
def open_mouth():


# Main (calling functions):

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

good_monster()
give_jar()
open_mouth()

# End (end of script)