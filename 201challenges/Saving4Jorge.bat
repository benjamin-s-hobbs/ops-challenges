:: Windows Batch Scripting
::

:: Script Name:                  Ops Challenge: Class08
:: Author:                       Ben Hobbs
:: Date of latest revision:      05/4/2023
:: Purpose:                      Create a batch file that recursively copies Jorge’s work files on his desktop (recursively meaning to include folder contents).


:: Declaration of variables


:: Declaration of functions


:: Main:

robocopy C:\Users\j.thompson\Desktop\*.* E:\AutoDesktop /rh:0000-0200 /s /z /dcopy:date /log+: jorgelog.txt

:: End