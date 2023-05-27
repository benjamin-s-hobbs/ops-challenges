#!/bin/bash

# Script Name:                  Ops Challenge: Class06 (ifthengo.sh)
# Author:                       Ben Hobbs
# Date of latest revision:      05/1/2023
# Purpose:                      Create a script that detects if a file or directory exists, then creates it if it does not exist.
#                               Your script must use at least one array, one loop, and one conditional.



# Declaration of variables
filebox=(var0++ )


# Declaration of functions

if test -f $varfilename ;
 then 

 echo "File is already there"
 else

 echo "File is around is somewhere... Hold on..."
 touch var1filename
 ls -a
 echo "Here it is. Found it."
fi


print_notsure () {
while [ "x${var1}" > x0 ] 
 do
    ls
    echo "How many are there?"
    read var1
    echo "Are you sure? I think you missed one...check again ${var1} can't be right!"
done

echo "Okay fine, but I'm telling him that it's your fault."
}

# Main:                          
echo "What are you looking for?"

read varfilename

if test -f $varfilename ;
 then 

 echo "File is already there"
 else

 echo "File is around is somewhere... Hold on..."
 touch var1filename
 ls -a
 echo "Here it is. Found it."
fi



# End