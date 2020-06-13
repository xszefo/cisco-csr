#!/usr/bin/python3

import requests

requests.packages.urllib3.disable_warnings()

host = 'ios-xe-mgmt-latest.cisco.com'
port = '9443'
username = 'developer'
password = 'C1sco12345'

def main():
	url = f'https://{host}:{port}/restconf/data/ietf-interfaces:interfaces'
	print(url)
	headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
	
	response = requests.get(url, auth=(username, password), headers=headers, verify=False)

	result = response.json()['ietf-interfaces:interfaces']['interface']
	
	for iface in result:
		print(10*"*")
		name = iface.get('name', 'none')
		descr = iface.get('description', 'none')
		print(f'{name} - {descr}')
		ip_add = iface.get('ietf-ip:ipv4').get('address')
		if ip_add is not None:
			ip = ip_add[0]['ip']
			mask = ip_add[0]['netmask']
			print(f'{ip} {mask}')
		else:
			print('Interface has no IP address')

if __name__ == '__main__':
	main()

