# Lab: Shodan API for Python
# Author: Branden Quach
# November 5, 2024
# Python program that queries Shodan for "'in-tank inventory' state:'AZ'"

import shodan
import json

api_key = 'AL1GnuNI2grRMXwnzWtLcbBzSrotpwE8'

api = shodan.Shodan(api_key)

def shodan_query(query):
    try:
        results = api.search(query)
        return results
    except shodan.APIError as e:
        print(f'Error: {e}')
        return None

  
