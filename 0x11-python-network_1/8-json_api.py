#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':

    data = {}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ''

    res = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        resJSON = res.json()
        if resJSON:
            print('{[]} {}'.format(resJSON.get('id'), resJSON.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
