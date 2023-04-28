#!/bin/bash

# Script Name:                  Ops Challenge: Class04
# Author:                       Ben Hobbs
# Date of latest revision:      04/27/2023
# Purpose:                      Creates four directories: dir1, dir2, dir3, dir4. Put the names of the four directories in an array
#                               Reference the array variable to create a new .txt file in each directory

# Declaration of variables
# Put the names of the four directories in an array
bigbox=(/home/ben142/ops-201d8-code-challenges/dir1  /home/ben142/ops-201d8-code-challenges/dir2 /home/ben142/ops-201d8-code-challenges/dir3 /home/ben142/ops-201d8-code-challenges/dir4)


# Declaration of functions
#Creates four directories: dir1, dir2, dir3, dir4
mkdir_new () { 
  mkdir dir1
  mkdir dir2
  mkdir dir3
  mkdir dir4
  touch ${bigbox[0]}/paper.txt 
  touch ${bigbox[1]}/paper.txt 
  touch ${bigbox[2]}/paper.txt 
  touch ${bigbox[3]}/paper.txt 
}
# Reference the array variable to create a new .txt file in each directory

# Main:                          
mkdir_new

# End