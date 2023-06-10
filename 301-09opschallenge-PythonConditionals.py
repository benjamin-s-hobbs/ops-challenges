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

# Nested if statement
if wind == "strong":
  print("It's a windy day.")
  if pollen_count > 70:
    print("It's windy and a high pollen count! Ah-choo!")
  elif pollen_count <= 70 and pollen_count > 30:
    print("Careful out there, it's windy with a moderate pollen count.")
  else:
    print("No worries, it may be windy but there is a low pollen count today.")
elif wind == "weak":
  print("The wind is calm today.")
else:
  print("Wind conditions are unknown.")

# Complex logical conditions
if forecast == "rain" or wind == "strong":
  print("The weather is too severe to be outside today!")
elif temperature > 75 and humidity > 70:
  print("It's hot and humid! Yuck!'")
elif not forecast == "rain" and temperature <= 50:
  print("This sounds like a perfect day.")
else:
  print("Weather conditions are unknown.")