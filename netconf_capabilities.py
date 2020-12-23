#!/usr/bin/python3

import ncclient.manager

host = 'ios-xe-mgmt.cisco.com'
port = '10000'
username = 'developer'
password = 'C1sco12345'

def main():
	print(f'Connecting to {host}...')

	m = ncclient.manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False)
    #with ncclient.manager.connect(host=host, port=netconf_port, 
    #                    username=username, 
    #                    password=password, 
    #                    hostkey_verify=False,
    #                    device_params = {'name': 'nexus'}) as m:
	if m.connected:
		print('Connected')
		with open('csr_capabilities', 'w') as f:

			for cap in m.server_capabilities:
				print(cap)
				f.write(cap)
				f.write('\n')

	
	m.close_session()
	
if __name__ == '__main__':
    main()
