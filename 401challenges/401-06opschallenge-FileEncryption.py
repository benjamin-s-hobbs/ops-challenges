#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-06opschallenge-FileEncryption.py
# Author:                       Ben Hobbs
# Date of latest revision:      07/17/2023
# Purpose:                      

# References:
import cryptography.fernet import Fernet

# Import Libraries


# Declaration of variables
# How to declare a variable in python
#   greeting = "Welcome to Python!"
# How to call a variable
#   print(greeting)



# Declaration of functions
# Write a function that handles key generation
def gen_key():

    # Generate a key.
    key = Fernet.generate_key()
    # Saving the generated key to a file for reuse.
    with open("key.key", "wb") as key_file:
        Key_file.write(key)      
# Write a function to load up the generated key so we can encrypt and decrypt
def load_key():

    # Retreives the generated key from the key.key file.
    return open("key.key", "r").read()

# Main:
# Generate and write the new key
write_key()

# Load the generated key
key = load_key()
print("Key is " + key)

# Encrypt a message

# Message to be encrypted
message = "THIS IS TOP SECRET!!"

print ("Plaintext message is" + message)

# DO THE ENCRYPTION - Initiatilize the Fernet modeule and names it "f"
f = Fernet(key)

#Encrypt your message
encrypted_message = f.encrypt(message)

# End