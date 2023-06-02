#!/bin/bash

# Script Name:                  Ops Challenge: 301Class03
# Author:                       Ben Hobbs
# Date of latest revision:      06/01/2023
# Purpose:                      To Create a new bash script that performs the following:
#                               Prompts user for input directory path.
#                               Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#                               Navigates to the directory input by the user and changes all files inside it to the input setting.
#                               Prints to the screen the directory contents and the new permissions settings of everything in the directory.



# Declaration of variables
varpath=()

# Declaration of functions

ch_perms(){

# Prompts user for input directory path.
echo "where is the file you want changed? (path)"

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
echo and what permissions do you want to give read$varpath?

# Navigates to the directory input by the user and changes all files inside it to the input setting.
echo "Okay, let's do it..."
chmod $varpath
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
cat 
}

# Main:                          


# End