#!/usr/bin/env python3.8

import requests
requests.packages.urllib3.disable_warnings()

host = 'ios-xe-mgmt.cisco.com'
port = '9443'
username = 'developer'
password = 'C1sco12345'

def get_root():
    url = 'https://ios-xe-mgmt.cisco.com:9443/.well-known/host-meta'
    response = requests.get(url, auth=(username, password), verify=False)

    if response.status_code == 200:
        print(response.text)


def get_detail():
    url = 'https://ios-xe-mgmt.cisco.com:9443/restconf'
    response = requests.get(url, auth=(username, password), verify=False)

    if response.status_code == 200:
        print('Top level resources:')
        print(response.text)

if __name__ == '__main__':
    get_root()
    get_detail()
