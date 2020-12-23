#!/usr/bin/python3

import requests

requests.packages.urllib3.disable_warnings()

host = 'ios-xe-mgmt.cisco.com'
port = '9443'
username = 'developer'
password = 'C1sco12345'

def main():
	url = f'https://{host}:{port}/restconf/data/ietf-routing:routing-state'
	print(url)
	headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
	
	response = requests.get(url, auth=(username, password), headers=headers, verify=False)

	print(response.status_code)
	result = response.json()['ietf-routing:routing-state']['routing-instance']
	
	for inst in result:
		name = inst['name']
		ribs = inst['ribs']['rib']
		print(f'VRF: {name}')
		
		for rib in ribs:
			routes = rib.get('routes', 'none')
			if routes != 'none':
				for route in routes['route']:
					dest = route['destination-prefix']
					next_hop_add = route['next-hop']['next-hop-address']
					next_hop_int = route['next-hop']['outgoing-interface']
					proto = route['source-protocol'].split(':')[1]
					print(f'{dest} via {next_hop_add} ({next_hop_int}) | Protocol: {proto}')
		print('\n')


if __name__ == '__main__':
	main()

