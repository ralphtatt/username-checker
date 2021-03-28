# username-checker
Checks if usernames are available on multiple sites, as specified in two files (See config section). 

This is set up to be a Lambda function, and includes a make file for generating the deployment zip and for deploying to AWS.

# Config
For both config files, make sure there is no newline, or else this will be included in the search

## `urls`
This file has the URLS that you would like to check, along with a $USERNAME variable for where the username goes in the URL.

## `usernames`
These are for the usernames that you would like to check for.

# Installation 

## Prerequisites
Make a virtual environment and install the packages in `requirements.txt`. 

## Building Deployment Folder
If you wouldn't like to use terraform, then the following command can be run to build the deployment package.

```
$VENV="<VENV_NAME>" make build-lambda
```

## Terraform
If you'd like to deploy the code on AWS, you can run `make plan` to see what will be deployed. If you're happy, then run `make build` and it will be deployed. 

# Future Changes

 - An SES resource needs to be added to automatically send an email when a change has been found.
 - Variables for changing deployment settings
