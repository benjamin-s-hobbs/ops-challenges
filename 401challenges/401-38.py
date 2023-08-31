#!/usr/bin/ python3
# the shebang line instructs the system to use the env command to locate the python3 
# interpreter and execute the script with it

# Script Name:                  Ops Challenge: 401-38.py XSS Vulnerability Detection with Python
# Author:                       Abdou Rockikz
# Modified by:                  Benjamin Hobbs
# Date of latest revision:      08/30/2023
# Purpose:                      Copy the DEMO.md file from class repo > class-38 > challenges and complete the TODOs.
#                               Fully annotate any missing comments and populate any missing variables/code
#                               Test the script in Web Security Dojo to confirm the output is correct
#                               This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame
#                               This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php

# References:
# Demo code Class38
# Marco Vazquez 401-Class38 topic intro 

### TODO: Install requests bs4 before executing this in Python3

# Import Libraries:
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin



# Declaration of variables (Global):


# Declaration of functions:

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
# def get_all_forms(url):
#     soup = bs(requests.get(url).content, "html.parser")
#     return soup.find_all("form")

# ### TODO: Add function explanation here ###
# ### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
# def get_form_details(form):
#     details = {}
#     action = form.attrs.get("action").lower()
#     method = form.attrs.get("method", "get").lower()
#     inputs = []
#     for input_tag in form.find_all("input"):
#         input_type = input_tag.attrs.get("type", "text")
#         input_name = input_tag.attrs.get("name")
#         inputs.append({"type": input_type, "name": input_name})
#     details["action"] = action
#     details["method"] = method
#     details["inputs"] = inputs
#     return details

# ### TODO: Add function explanation here ###
# ### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
# def submit_form(form_details, url, value):
#     target_url = urljoin(url, form_details["action"])
#     inputs = form_details["inputs"]
#     data = {}
#     for input in inputs:
#         if input["type"] == "text" or input["type"] == "search":
#             input["value"] = value
#         input_name = input.get("name")
#         input_value = input.get("value")
#         if input_name and input_value:
#             data[input_name] = input_value

#     if form_details["method"] == "post":
#         return requests.post(target_url, data=data)
#     else:
#         return requests.get(target_url, params=data)

# ### TODO: Add function explanation here ###
# ### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
# def scan_xss(url):
#     forms = get_all_forms(url)
#     print(f"[+] Detected {len(forms)} forms on {url}.")
#     js_script = ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text.
#     is_vulnerable = False
#     for form in forms:
#         form_details = get_form_details(form)
#         content = submit_form(form_details, url, js_script).content.decode()
#         if js_script in content:
#             print(f"[+] XSS Detected on {url}")
#             print(f"[*] Form details:")
#             pprint(form_details)
#             is_vulnerable = True
#     return is_vulnerable


# # Main (calling functions):

# ### TODO: Add main explanation here ###
# ### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
# if __name__ == "__main__":
#     url = input("Enter a URL to test for XSS:") 
#     print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection


# End (end of script)