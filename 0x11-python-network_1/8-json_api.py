#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except ValueError:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except ValueError:
        print("Not a valid JSON")
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    q = sys.argv[1] if len(sys.argv) >= 2 else ""

    response = requests.post(url, data={'q': q})
    try:
        r_dict = response.json()
        if r_dict:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
