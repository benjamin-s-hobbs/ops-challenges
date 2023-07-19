#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-07opschallenge-FileEncryption.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/18/2023
# Purpose:                      Add a feature capability to your script to:
#                               Recursively encrypt a single folder and all its contents.
#                               Recursively decrypt a single folder that was encrypted by this tool.
#                               
# References:


# Import Libraries
from cryptography.fernet import Fernet

# Declaration of variables (global)
# Value of key is assigned to a variable
f = Fernet(key)
# The plaintext is converted = ciphertext
token =f.encrypt(b"welcome to cybersecurity")

# Decrypting the ciphertext = plaintext
d = f.decrypt(token)


# Declaration of functions

# Write a function to encrypt a message
def encrypt_message():

    # Generate a key.
    key = Fernet.generate_key()

    # Saving the generated key to a file for reuse.
    with open("key.key", "wb") as key_file:
        key_file.write(key)      

    # Write a function to load up the generated key so we can encrypt and decrypt
    def load_key():

        # Retreives the generated key from the key.key file.
        return open("key.key", "rb").read()
    # Function to encrypt a message

    # Function to decrypt a message

    # Function to encrypt a file

    encrypted_file = f.encrypt(file.data)
    # Function to decrypt a file
    
    # Function to create a user menu for the above options

# Function to encrypt a folder (recursively)

# Function to decrypt a folder (recursively)

# Modification to function menu to add additonal options

    # Main:
  

    
    
    
    # End