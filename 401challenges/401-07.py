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
# JUDICIOUS help from Marco...really loving the way he breaks down the thought process of creating functions (solution in class)
# https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/

# Import Libraries
from cryptography.fernet import Fernet
from os.path import exists
import os

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