# Script Name:                    Ops Challenge: 301Class13opschallenge-PS_ADAutomation.ps1
# Author:                         Ben Hobbs
# Date of latest revision:        6/15/2023
# Purpose:                      
#
#
# Declaration of variables:

$VarNewName = "Franz Ferdinand"
$VarTitle = "TPS Reporting Lead"
$VarCompany = "GlobeX USA"
$VarDept = "TPS Department"
$VarWhere = "Springfield, OR"
$VarEmail = "ferdi@GlobeXpower.com"

#
#
# Declaration of functions:
#

function Get-GlobexNewGuy {

# Write-Output "Ok, let's add you to the system."
# Write-Output "What's your full name? (First Name, Last Name)"
# read=varnewname
# Write-Output "What's your title?"
# read=vartitle
# Write-Output "What company are you with?"
# read=varcompany
# Write-Output "Department?"
# read=vardept
# Write-Output "Where will your location be?"
# read=varwhere
# Write-Output "And what will your email address be?"
# read=varemail

New-ADUser -Name $VarNewName 

Write-Output "New User Added"
Write-Output "Please verify the details"

print($varNewName)
#    #print($vartitle)
#    print($vardept)
#    print($varcompany)
#    print($varwhere)
#    print($varemail)

Write-Output "Thank you. Welcome to GlobeX...Get to work."

}


# Main:

Get-GlobexNewGuy

# End:
