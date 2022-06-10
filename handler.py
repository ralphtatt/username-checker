import json
import urllib3
import time

http = urllib3.PoolManager()


def get_usernames():
    usernames = []
    for name in open("./usernames", "r"):
        usernames.append(name[:-1].lower())  # Removes newline from end and changes to lowercase
    return usernames[:-1]  # Removes newline from end


def get_domains():
    domains = []
    for domain in open("./domains", "r"):
        domains.append(domain[:-1].lower())  # Removes newline from end
    return domains[:-1]  # Removes newline from end


def generate_urls(usernames, domains):
    urls = []
    for username in usernames:
        for domain in domains:
            urls.append(domain.replace("$usercase", username))
    return urls


def get_available_usernames(urls):
    available = []
    for address in urls:
        response = http.request("GET", address)
        if response.status == 404:
            available.append(address)
    return available


def main(event, context):
    start_time = time.time()

    usernames = get_usernames()
    domains = get_domains()
    urls = generate_urls(usernames, domains)
    available = get_available_usernames(urls)

    print(f"Total time: {time.time() - start_time}s")

    return {
        'statusCode': 200,
        'body': json.dumps(available)
    }
