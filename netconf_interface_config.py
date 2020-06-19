#!/usr/bin/python3

import ncclient.manager

host = 'ios-xe-mgmt-latest.cisco.com'
port = '10000'
username = 'developer'
password = 'C1sco12345'

def main():
	print(f'Connecting to {host}...')
	filter ="""
		<filter>
 			<interfaces xmlns=”urn:ietf:params:xml:ns:yang:ietf-interfaces”>
  				<interaface>
   					<name>GigabitEthernet3</name>
  				</interface>
 			</interfaces>
		</filter>
	"""
	print(filter)
	m = ncclient.manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False)
	if m.connected:
		reply = m.get_config("running", filter)
		print(reply)
		print(dir(m))
	
	
if __name__ == '__main__':
    main()
