#!/bin/bash

# Script Name:                  Ops Challenge: Class05
# Author:                       Ben Hobbs
# Date of latest revision:      04/28/2023
# Purpose:                      To write a script that displays running processes, asks the user for a PID, and then kills the process with that PID;
#                               while using a loop in your script


# Declaration of variables


# Declaration of functions

run_joshua () {
ps 
echo "What PID number would you like to choose?"
read var1
kill $var1
echo "Thank you Professor Falken, PID ${var1} has been destroyed. Resuming DEFCON1"
# Loops (while loop) back to step 1 and continues until user exits with Ctrl + C
while [ "x${var1}" > x0 ]
do
    ps 
    echo "What PID number would you like to choose?"
    read var1
    kill ${var1}
    echo "Thank you Professor Falken, PID ${var1} has been destroyed. Resuming DEFCON1"
done

echo "An interesting game. The only winning move is not to play. How about a nice game of chess?"

}

# Main:                          
run_joshua

# End