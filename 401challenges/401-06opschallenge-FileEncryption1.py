#!/usr/bin/env/python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-06opschallenge-FileEncryption.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/17/2023
# Purpose:                      In Python, create a script that utilizes the cryptography library to:
#                               Prompt the user to select a mode:
#                               Encrypt a file      (mode 1)
#                               Decrypt a file      (mode 2)
#                               Encrypt a message   (mode 3)
#                               Decrypt a message   (mode 4)
#                               If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#                               If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#                               Depending on the selection, perform one of the below functions. 
#
#                               You’ll need to create four functions:
#                               Encrypt the target file if in mode 1.
#                               Delete the existing target file and replace it entirely with the encrypted version.
#                               Decrypt the target file if in mode 2.
#                               Delete the encrypted target file and replace it entirely with the decrypted version.
#                               Encrypt the string if in mode 3.
#                               Print the ciphertext to the screen.
#                               Decrypt the string if in mode 4.
#                               Print the cleartext to the screen.

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

    # Main:
    # Check to see if a key exists already

    # Generate and write the new key
    key = Fernet.generate_key()

    # Load the generated key
    key = load_key()
    print("Key is " + str(key.decode('utf-8')))



    # Message to be encrypted
    message = "THIS IS TOP SECRET!!"

    print ("Plaintext message is" + message)

    # DO THE ENCRYPTION - Initiatilize the Fernet modeule and names it "f"
    f = Fernet(key)

    #Encrypt your message
    encrypted_message = f.encrypt(message)

    #Print the encrypted message
    print()

    # End