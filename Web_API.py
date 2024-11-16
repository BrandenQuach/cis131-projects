# Lab: Web API for Gmail and Sinch
# Author: Branden Quach
# November 15, 2024
# Python program that queries Shodan for "'in-tank inventory' state:'AZ'", then emails report and sends an SMS.

# Libraries
import shodan, json, ezgmail, os

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

# Creates variable for email body
email_body = 'In-tank Inventory for Arizona report:\n'

for result in results['matches']:
    # Prints data of all results into email body variable
    email_body += f"{result['data']}"

# Sends email containing in-tank report
ezgmail.send('bquach@mail.pima.edu', 'In-tank Inventory for Arizona', email_body)

# Runs sinch to send SMS
runfile('send-sms.py')
