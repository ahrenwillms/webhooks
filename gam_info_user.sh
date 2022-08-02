#!/bin/bash

# Call the gam command and store the output as a variable
RESULT=$(/home/administrator/bin/gam/gam info user $1 | grep -E 'User:|Suspended|Org\ Unit' 2>/dev/null)

# Store the exit code as a variable
EXIT_CODE=$?

# Print a message based on the exit code
case "$EXIT_CODE" in

0) echo "$RESULT" ;;

148) echo "User does not exist" ;;

*) echo "User status unknown" ;;

esac

exit 0