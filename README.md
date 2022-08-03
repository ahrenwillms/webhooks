# webhooks
This is a collection of scripts used with the [webhook](https://github.com/adnanh/webhook) project to call scripts based on HTTP requests

| Filename | Description |
| ----------- | ----------- |
| [gam_create_user.py](https://github.com/ahrenwillms/webhooks/blob/main/gam_create_user.py) | A Python script to create a Google Workspace user. Accepts a JSON object as input. |
| [gam_info_user.sh](https://github.com/ahrenwillms/webhooks/blob/main/gam_info_user.sh) | A Bash script to output a Google Workspace user's info. Accepts a username string as input. |
| [gam_update_user.py](https://github.com/ahrenwillms/webhooks/blob/main/gam_update_user.py) | A Python script to update a Google Workspace user. Accepts a JSON object as input. |
| [update_both_passwords.sh](https://github.com/ahrenwillms/webhooks/blob/main/update_both_passwords.sh) | A Bash script with an inline [expect](https://man7.org/linux/man-pages/man1/expect.1.html) script to update a user's password in both Google Workspace and a macOS Open Directory Server. Accepts username and password strings as input. |
| [update_user_password.py](https://github.com/ahrenwillms/webhooks/blob/main/update_user_password.py) | A Python script to update the currently assigned user's password based on a device's serial number. Queries a FileMaker Server using FileMaker's [Data API](https://help.claris.com/en/data-api-guide/content/index.html). Accepts a serial number string as input. |
| [webhook.conf](https://github.com/ahrenwillms/webhooks/blob/main/webhook.conf) | A sample configuration file for [webhook](https://github.com/adnanh/webhook). |