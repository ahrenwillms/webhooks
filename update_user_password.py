#!/usr/bin/python3

#########################################################################################
# Webhook that queries FileMaker Server to retrieve username and password
# The username and password are passed to a second webhook script in order to update 
# a user's password on Google Workspace and Open Directory
#
# Requires Python 3 and requests module to be installed
#########################################################################################

import sys
import requests

# Store the script's first argument as a serial number variable
serial_number = sys.argv[1] if len(sys.argv) > 1 else "Invalid Serial Number"

print(f"Serial number is: {serial_number}")

#########################################################################################
# Query FileMaker Data API and store result
#########################################################################################

# Log in to FileMaker Server
login_url = 'https://FILEMAKER_SERVER_URL/fmi/data/v1/databases/DATABASE_FILE_NAME/sessions'
login_headers = {'Content-Type': 'application/json'}
login_result = requests.post(login_url, headers=login_headers, auth=('USERNAME', 'PASSWORD'))

login_response = login_result.json()
token = login_response["response"]["token"]

query_data = {
    "query":[
        {"Assets::hardware_serial_num": serial_number}
        ]
    }

# Search FileMaker database for serial number
query_url = 'https://FILEMAKER_SERVER_URL/fmi/data/v1/databases/DATABASE_FILE_NAME/layouts/LAYOUT_NAME/_find'
query_headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
query_result = requests.post(query_url, headers=query_headers, json=query_data)

# Convert the result to JSON
query_response = query_result.json()

# Store field data as variables
computer_name = query_response["response"]["data"][0]["fieldData"]["computer_name"]
username = query_response["response"]["data"][0]["fieldData"]["Users::username"]
password = query_response["response"]["data"][0]["fieldData"]["Users::current_password"]
status = query_response["response"]["data"][0]["fieldData"]["status"]

# Print value(s) for debugging
print(f"Computer name from FileMaker Server is: {computer_name}")

# Log out of FileMaker Server
logout_url = f'https://FILEMAKER_SERVER_URL/fmi/data/v1/databases/DATABASE_FILE_NAME/sessions/{token}'
logout_result = requests.delete(logout_url, data='')

#########################################################################################
# Call webhook to update password on Google Workspace and Open Directory
#########################################################################################

if status == "Assigned":
    print("Computer is assigned. Updating password.")
    
    webhook_query_data = {"username": username, "password": password}
    webhook_request_url = 'https://WEBHOOK_SERVER_URL/hooks/update-both-passwords'
    webhook_headers = {'Content-Type': 'application/json'}
    
    webhook_result = requests.post(webhook_request_url, headers=webhook_headers, auth=('USERNAME', 'PASSWORD'), json=webhook_query_data)
else:
    print("Computer is not assigned. Skipping password update")

sys.exit(0)
