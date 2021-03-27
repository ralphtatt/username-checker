import json
import requests
import time
from itertools import product
from string import ascii_lowercase

def get_specified_usernames():
    usernames = []
    for name in open("./usernames", "r"):
        usernames.append(name[:-1]) # Removes newline from end
    return usernames

def generate_two_letter_usernames():
    two_letter = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]
    return two_letter 

def get_urls():
    urls = []
    for url in open("./urls", "r"):
        urls.append(url[:-1])
    return urls

def generate_paths(usernames, urls):
    paths = []
    for username in usernames:
        for url in urls:
            paths.append(url.replace("$USERNAME", username))
    return paths

def find_available_usernames(paths):
    available = []
    for address in paths:
        response = requests.get(address)
        if response.status_code == 404:
            available.append(address)
    return available

def lambda_handler(event, context):
    start_time = time.time()

    specified_usernames = get_specified_usernames()
    two_letter_usernames = generate_two_letter_usernames()
    usernames = specified_usernames + two_letter_usernames
    urls = get_urls()
    paths = generate_paths(usernames, urls)
    available = find_available_usernames(paths)

    print(f"Total time: {time.time() - start_time}")

    return {
        'statusCode': 200,
        'body': json.dumps(available)
    }

