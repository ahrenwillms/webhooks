#!/usr/bin/python3

import sys
import json
import subprocess

# Store JSON input from webhook into a variable
data = json.loads(sys.argv[1])

# Store JSON data as variables
username = data["username"]
password = data["password"]
firstname = data["firstname"]
lastname = data["lastname"]
org = data["org"]

# Call the gam command and store its exit code as a variable
gam_command_output = subprocess.call(["/home/administrator/bin/gam/gam", "create", "user", username, "password", password, "firstname", firstname, "lastname", lastname, "org", org])

# Print a message based on the exit code
if gam_command_output == 0 :
    print ("User account created")
elif gam_command_output == 153 :
    print ("Error creating account: Account already exists")
else :
    print ("Unknown error")

sys.exit(0)