# username-checker
Checks if usernames are available on multiple sites. 

This is set up to be a Lambda function, and includes a make file for generating the deployment zip.

# Config
For both config files, make sure there is no newline, or else this will be included in the search

## `urls`
This file has the URLS that you would like to check, along with a $USERNAME variable for where the username goes in the URL.

## `usernames`
These are for the usernames that you would like to check for.

# Installation 
Make a virtual environment and install the packages in `requirements.txt`.

Then the following command can be run to build the deployment package.

```
$VENV="<VENV_NAME>" make build-lambda
```

# Future Changes

There will be terraform code added to automatically build this, with a cloudwatch event to automatically run this lambda hourly and an SNS topic that will email whenever anything is ready.

