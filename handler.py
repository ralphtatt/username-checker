import json
import urllib3
import time

http = urllib3.PoolManager()

def get_specified_usernames():
    usernames = []
    for name in open("./usernames", "r"):
        usernames.append(name[:-1]) # Removes newline from end
    return usernames

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
        response = http.request("GET", address)
        if response.status == 404:
            available.append(address)
    return available

def main(event, context):
    start_time = time.time()

    usernames = get_specified_usernames()
    urls = get_urls()
    paths = generate_paths(usernames, urls)
    available = find_available_usernames(paths)

    print(f"Total time: {time.time() - start_time}s")

    return {
        'statusCode': 200,
        'body': json.dumps(available)
    }

