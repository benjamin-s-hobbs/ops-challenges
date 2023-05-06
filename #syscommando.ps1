# Script Name:                  Ops Challenge: Class10 (syscommando.ps.1)
# Author:                       Ben Hobbs
# Date of latest revision:      05/05/2023
# Purpose:                      To write a set of Powershell commands that fetch info about running processes, open processes, and close processes; while
#                               including language appropriate syntax and file extensions.

# Declaration of variables

# Declaration of functions

# Main:                

# Remember to follow this class’s commenting requirements on all scripts.

# Create a Powershell script that performs these operations on separate lines. 
# The overall script is not designed to operate holistically, but rather act as a reference for how to execute various 
# interesting operations with the process family of Powershell commandlets. 
# Clearly indicate with comments each component below.

# Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object CPU -Descending

# Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object ID -Descending

# Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Select-Object -First 5 | Sort-Object WorkingSet64 -Descending

# Start a browser process (such as Google Chrome or MS Edge) and have it open https://owasp.org/www-project-top-ten/.


# Start the process Notepad ten times using a for loop.


# Close all instances of the Notepad.
Stop-Process -Name "Notepad" -PassThru

# Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, 
#such as Google Chrome or MS Edge.
Stop-Process -Id 5667 -Confirm -PassThru


# End