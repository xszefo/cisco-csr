#!/usr/bin/python3

import requests

requests.packages.urllib3.disable_warnings()

host = 'ios-xe-mgmt.cisco.com'
port = '9443'
username = 'developer'
password = 'C1sco12345'

def main():
	url = f'https://{host}:{port}/restconf/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data/'
	print(url)
	headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
	
	response = requests.get(url, auth=(username, password), headers=headers, verify=False)

	print(response.status_code)
	result = response.json()['Cisco-IOS-XE-device-hardware-oper:device-hardware-data']['device-hardware']
	
	inventory = result['device-inventory']
	system_data = result['device-system-data']	

	for elem in inventory:
		dev_name = elem['dev-name']
		sn = elem['serial-number']
		descr = elem['hw-description']
		print(f'{dev_name} - {descr} | SN: {sn}')
	
	print(10*"*")
	curr_time = system_data['current-time'].replace('T', ' ')
	boot_time = system_data['boot-time'].replace('T', ' ')
	last_reboot = system_data['last-reboot-reason']
	
	print(f'Current time: {curr_time}')
	print(f'Boot time: {boot_time}')
	print(f'Last reboot reason: {last_reboot}')

if __name__ == '__main__':
	main()

