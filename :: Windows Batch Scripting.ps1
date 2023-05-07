#Eventloggin 
#Windows Batch Scripting

# Script Name:                  Ops Challenge: Class09
#Author:                       Ben Hobbs
# Date of latest revision:      05/04/2023
# Purpose:                      Write a set of Powershell commands that fetch useful System event logs 
#                               and include language appropriate syntax and file extensions.

# Declaration of variables

# Declaration of functions

# Main:  

# Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt.
$Begin = Get-Date -Date '5/4/2023 09:00:00'
$End = Get-Date -Date '5/5/2023 09:00:00'
Get-EventLog -LogName System -After $Begin -Before $End | Out-File -Path \\Desktop\last_24.txt

# Output all “error” type events from the System event log to a file on your desktop named errors.txt.
Get-EventLog -LogName System -EntryType Error | Out-File -Path \Desktop\errors.txt

# Print to the screen all events with ID of 16 from the System event log.
Get-EventLog -LogName -EventID 16 

# Print to the screen the most recent 20 entries from the System event log.
Get-EventLog -LogName System -Newest 20

# Print to the screen all sources of the 500 most recent entries in the System event log. Ensure that the full lines are displayed (get rid of the … and show the entire text)
Get-EventLog -LogName System -Newest 500 

# End