# username-checker
Checks if usernames are available on multiple sites, as specified in two files (See config section). 

## Deployment
It is deployed using [Serverless](https://www.serverless.com/) framework. 

Clone the repo and run `sls deploy` to setup.

## Config
### `domains`
This file has the domains that you would like to check, along with a $USERNAME variable for where the username goes in the URL.

Example:
```
https://github.com/$USERNAME
https://twitter.com/$USERNAME
```

### `usernames`
These are for the usernames that you would like to check for.

Example:
```
username
user-name
```
There are no checks for if the username is valid for the site, which may return a false match for an available username.