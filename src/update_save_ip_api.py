#!/usr/bin/env python3

import time
import os
import sys
import urllib.parse
import requests
import schedule

IPIFY_URL = 'https://api.ipify.org'
KEY_ENVNAME = 'SAVEIPAPI_KEY'
BASEURL_ENVNAME = 'SAVEIPAPI_BASEURL'
APIKEY_ENVNAME = 'SAVEIPAPI_APIKEY'

KEY = os.getenv(KEY_ENVNAME)
BASEURL = os.getenv(BASEURL_ENVNAME)
APIKEY = os.environ.get(APIKEY_ENVNAME)


def job():
    try:
        success, ip = get_public_ip()
        if success:
            post_ip(ip)
        else:
            print('Unable to get public ip from ipify.')
    except Exception as e:
        print (f'Error: Unable to get or send ip: {e}')


def get_public_ip():
    response = requests.get(IPIFY_URL, timeout=10)
    if response.status_code != 200:
        print(f'Recieved status code {response.status_code} from ipify.')
    success = response.status_code == 200
    ip = response.content.decode('ascii')
    return (success, ip)


def post_ip(ip):
    post_headers = { 'ApiKey': APIKEY }
    post_content = { 'ip': ip }

    response = requests.post(
        urllib.parse.urljoin(BASEURL, f'/ip/{KEY}'),
        headers=post_headers,
        json=post_content,
        timeout=10)
    if response.status_code == 200:
        print(f'Sent ip {ip} to {BASEURL}')
    else:
        print(f'Unable to send ip. Server replied with status {response.status_code}.')


def check_environment_variables():
    if KEY == None:
        print(f'Unable to find environment variable for {KEY_ENVNAME}. Program ends.')
        sys.exit(1)
    if BASEURL == None:
        print(f'Unable to find environment variable for {BASEURL_ENVNAME}. Program ends.')
        sys.exit(1)
    if APIKEY == None:
        print(f'Unable to find environment variable for {APIKEY_ENVNAME}. Program ends.')
        sys.exit(1)


if __name__ == '__main__':
    check_environment_variables()
    print('Starting Application.')
    
    try:
        job()

        schedule.every(1).hours.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program interupted by user')
        sys.exit(0)
