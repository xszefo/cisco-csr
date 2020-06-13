#!/usr/bin/python3

import requests

requests.packages.urllib3.disable_warnings()

host = 'ios-xe-mgmt-latest.cisco.com'
port = '9443'
username = 'developer'
password = 'C1sco12345'

def main():
	url = f'https://{host}:{port}/restconf/data/openconfig-system:system/'
	print(url)
	headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
	
	response = requests.get(url, auth=(username, password), headers=headers, verify=False)

	print(response.status_code)
	result = response.json()
	print(result)
	
	



if __name__ == '__main__':
	main()

