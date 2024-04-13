#!/usr/bin/env python3

import time
import os
import sys
import requests
import schedule

KEY = os.getenv('SAVEIPAPI_KEY')
HOSTNAME = os.getenv('SAVEIPAPI_HOSTNAME')
APIKEY = os.environ.get('SAVEIPAPI_APIKEY')


if KEY == None:
    print('Unable to find environment variable for SAVEIPAPI_KEY. Program ends.')
    sys.exit(1)
if HOSTNAME == None:
    print('Unable to find environment variable for SAVEIPAPI_HOSTNAME. Program ends.')
    sys.exit(1)
if APIKEY == None:
    print('Unable to find environment variable for SAVEIPAPI_APIKEY. Program ends.')
    sys.exit(1)

def job():
    try:
        response = requests.get('https://api.ipify.org', timeout=10)
        ip = response.content.decode('ascii')

        post_headers = { 'ApiKey': APIKEY }
        post_content = { 'ip': ip }

        response = requests.post(
            f'https://{HOSTNAME}/ip/{KEY}',
            headers=post_headers,
            json=post_content,
            timeout=10)
        if response.status_code == 200:
            print(f'Sent ip {ip} to {HOSTNAME}')
        else:
            print(f'Unable to send ip. Server replied with status {response.status_code}.')
    except Exception as e:
        print (f'Error: Unable to get or send ip: {e}')

schedule.every(1).hours.do(job)

if __name__ == '__main__':
    print('Starting Application.')
    while True:
        schedule.run_pending()
        time.sleep(1)
