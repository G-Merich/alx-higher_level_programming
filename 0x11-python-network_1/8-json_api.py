#!/usr/bin/python3
"""
    Python script, POST request to http://0.0.0.0:5000/search_user;
"""

import requests
from sys import argv
if __name__ == "__main__":
    json = {'q': ""}
    if len(argv) > 1:
        json['q'] = argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", json)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if response.json():
            print("[{}] {}".format(response.json().get('id'),
                  response.json().get('name')))
        else:
            print("No result")
