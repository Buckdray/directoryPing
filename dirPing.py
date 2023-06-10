#!/usr/bin/env python3
import requests
def wordlist():
    with open('wordlist.txt', 'r') as file:
        words = [line.strip() for line in file]
    return words
def request(path):
    base_url = 'http://IP'
    url = base_url + path
    try:
        response = requests.get(url)
        if response.status_code != 404:
            print(f'[{response.status_code}]:\t{url}')
    except Exception as e:
        pass
    
for i in wordlist():
    request(i)