#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 interpreter and execute the script with it

# Script Name:                  Ops Challenge: 301Class09opschallenge-PythonConditonals.py
# Author:                       Ben Hobbs
# Date of latest revision:      06/9/2023
# Purpose:                      Create if statements using these logical conditionals below. 
#                               Each statement should print information to the screen depending on if the condition is met:
#                               Equals: a == b
#                               Not Equals: a != b
#                               Less than: a < b
#                               Less than or equal to: a <= b
#                               Greater than: a > b
#                               Greater than or equal to: a >= b
#                               Create an if statement using a logical conditional of your choice and include 
#                               elif keyword that executes when other conditions are not met.
#                               Create an if statement that includes both elif and else to execute when both if 
#                               and elif are not met.


# Import Libraries
import os

# Declaration of variables
# How to declare a variable in python
#   greeting = "Welcome to Python!"
# How to call a variable
#   print(greeting)

prediction = "victory"
pitch = "muddy"
crowd = 10,000
competition = "strong"
strikers = "exceptional"
midfield = "average"
backs = "above average"
keepers = "solid"

# Declaration of functions

if prediction == "victory":
  print("They think you'll win...don't get cocky!")

if pitch == "muddy":
  print("The pitch is a bit soft today, so adjust your runs accordingly.")
else:
  print("The pitch is firm, run like the wind!")

if crowd == 10000:
  print("Decent crowd...a wonderful day for football!")
elif crowd < 10000:
  print("Where is everybody? The crowd is a bit thin today!")  
elif crowd > 10000:
  print("Whoa, look at this crowd. It's a packed house today!")


# Main:
                     



# End