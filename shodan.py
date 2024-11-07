# Lab: Shodan API for Python
# Author: Branden Quach
# November 6, 2024
# Python program that queries Shodan for "'in-tank inventory' state:'AZ'"

# Libraries
import shodan
import json

# API key for shodan
api_key = 'AL1GnuNI2grRMXwnzWtLcbBzSrotpwE8'

# Links API key to shodan
api = shodan.Shodan(api_key)

# Search query
query = "'in-tank inventory' state:'AZ'"

# Shodan search query function
def shodan_query(query):
    try:
        # Collects and returns results of query
        results = api.search(query)
        return results
    # Loop for errors
    except shodan.APIError as e:
        print(f'Error: {e}')
        return None

# Sets query results
results = shodan_query(query)

# Selects all results that matches query
for result in results['matches']:
    # Prints data of all results
    print(f"{result['data']}")
