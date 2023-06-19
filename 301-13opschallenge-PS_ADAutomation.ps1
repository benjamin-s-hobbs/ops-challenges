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
$VarCity = "Springfield"
$VarState = "OR"
$VarEmail = "ferdi@GlobeXpower.com"
$VarPass = "ScatterSenbonSakura06!"
#
#
# Declaration of functions:
#

function Get-GlobexNewGuy {

 Write-Output "Ok, let's add you to the system."
 $VarNewName = Read-Host "What's your full name? (First Name, Last Name)"
 Write-Output "Franz Ferdinand"
 $VarTitle = Read-Host "What's your title?"
 Write-Output "TPS Reporting Lead"
 $VarCompany = Read-Host "What company are you with?"
 Write-Output "GlobeX USA"
 $VarDept =  Read-Host "Department?"
 Write-Output "TPS Department"
 $VarCity = Read-Host "Where will your location be? (City)"
 Write-Output "Springfield"
 $VarState = Read-Host "And what State?"
 Write-Output "OR"
 $VarEmail = Read-Host "And what will your email address be?"
 Write-Output "ferdi@GlobeXpower.com"
 $VarPass = Read-Host "Enter a password" -AsSecureString

New-ADUser -Name $VarNewName -Title $VarTitle -Company $VarCompany -Department $VarDept -City $VarCity 
-State $VarState -EmailAddress $VarEmail -AccountPassword $VarPass

Write-Output "New User Added"
Write-Output "Please verify the details"

Write-Output $VarNewName
Write-Output $VarTitle
Write-Output $VarDept
Write-Output $VarCompany
Write-Output $VarWhere
Write-Output $VarEmail
Write-Output $VarPass

Write-Output "Thank you. Welcome to GlobeX...Get to work."

}


# Main:

Get-GlobexNewGuy

# End:
