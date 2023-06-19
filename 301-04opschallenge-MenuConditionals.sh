#!/bin/bash

# Script Name:                  Ops Challenge: 301Class04
# Author:                       Ben Hobbs
# Date of latest revision:      06/02/2023
# Purpose:                      To create a bash script that launches a menu system with the following options:
#                                  * Hello world (prints “Hello world!” to the screen)
#                                  * Ping self (pings this computer’s loopback address)
#                                  * IP info (print the network adapter information for this computer)
#                                  * Exit
#                               Next, the user input should be requested.
#                               The program should next use a conditional statement to evaluate the user’s input, 
#                               then act according to what the user selected.
#                               Use a loop to bring up the menu again after the request has been executed.



# Declaration of variables


# Declaration of functions


get_menu() {

 while true; do
    clear
    echo "1. Print Hello World!"
    echo "2. Ping Self"
    echo "3. Print IP info"
    echo "4. Exit"
    read choice 
    
    if [[ $choice == 1 ]] ; then
        echo "Hello World!"
        read -p "Press Enter to continue"

    elif [[ $choice == 2 ]] ; then
        ping 127.0.0.1
        read -p "Press Enter to continue"

    elif [[ $choice == 3 ]] ; then
       ifconfig
       read -p "Press Enter to continue"
       
    elif [[ $choice == 4 ]] ; then
       echo "No problem, come back soon please!"
       read -p "Press Enter to continue"
       exit0
    else
       echo "Invalid choice"
       read -p "Press Enter to continue"
    fi
 done
}
# Main:                          

get_menu

# End

