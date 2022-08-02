#!/bin/bash

# Store username and password as varaibles
username=$1
password=$2

# Call the gam command to update the user's password
/home/administrator/bin/gam/gam update user "$username"@YOUR_DOMAIN.TLD password "$password"

#########################################################################################
# The following in an inline expect script used to update a user's password on a macOS
# Open Directory server. Passwordless SSH is used to establish an SSH session with
# the server. 
#########################################################################################

/usr/bin/expect -c "

# Set a timeout in the event that authentication fails
set timeout 60

# Spawn SSH session
spawn ssh -i /home/administrator/.ssh/id_rsa admin@YOUR_OPEN_DIRECTORY_SERVER.TLD 

# The prompt on the Open Directory Server
expect \"HOSTNAME:~ admin$ \"

# Send the pwpolicy command with the username and password variables
send \"pwpolicy -a diradmin -u $username -setpassword $password \r\"

# The prompt for the directory admin password
expect \"Password for authenticator diradmin:\"

# Send the directory admin password
send \"YOUR_DIRADMIN_PASSWORD\r\"

# Send the exit command to disconnect from the server
send \"exit\r\"

expect eof"

exit 0