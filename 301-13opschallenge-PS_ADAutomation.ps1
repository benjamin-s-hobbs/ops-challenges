# Script Name:                    Ops Challenge: 301Class13opschallenge-PS_ADAutomation.ps1
# Author:                         Ben Hobbs
# Date of latest revision:        6/15/2023
# Purpose:                      
#
#
# Declaration of variables:

varnewname=("Franz Ferdinand")
vartitle=("TPS Reporting Lead")
varcompany=("GlobeX USA")
vardept=("TPS Department")
varwhere=("Springfield, OR")
varemail=("ferdi@GlobeXpower.com")

#
#
# Declaration of functions:
#

GlobexNewguy_(function) {

# echo "Ok, let's add you to the system."
# echo "What's your full name? (First Name, Last Name)"
# read=varnewname
# echo "What's your title?"
# read=vartitle
# echo "What company are you with?"
# read=varcompany
# echo "Department?"
# read=vardept
# echo "Where will your location be?"
# read=varwhere
# echo "And what will your email address be?"
# read=varemail

New-ADUser -Name $varnewname -OtherAttributes @{'title'=$vartitle;'EmailAddress'=$varemail;'City'=$varwhere;'Company'=$varcompany;'Department'=$vardept}

echo "New User Added"
echo "Please verify the details"

print($varnewname)
print($vartitle)
print($vardept)
print($varcompany)
print($varwhere)
print($varemail)

echo "Thank you. Welcome to GlobeX...Get to work."

}


# Main:



# End:
