#!/bin/bash

# Script Name:                  Ops Challenge: Class04
# Author:                       Ben Hobbs
# Date of latest revision:      04/27/2023
# Purpose:                      Creates four directories: dir1, dir2, dir3, dir4. Put the names of the four directories in an array
#                               Reference the array variable to create a new .txt file in each directory

# Declaration of variables
#Put the names of the four directories in an array
group=("dir" "dir1" "dir2" "dir3")

# Declaration of functions
#Creates four directories: dir1, dir2, dir3, dir4
new=mkdir {dir}
#Reference the array variable to create a new .txt file in each directory
createm=touch newtextfile.txt ${group[0-3]}

# Main:                          
echo new 
echo new
echo new
echo new

createm

# End