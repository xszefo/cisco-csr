#!/usr/bin/python3

import ncclient.manager
from lxml import etree

host = 'ios-xe-mgmt-latest.cisco.com'
port = '10000'
username = 'developer'
password = 'C1sco12345'

def main():
	print(f'Connecting to {host}...')
	filter ="""
	<native>
		<version>
		</version>
	</native>
	"""
	print(filter)
	m = ncclient.manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False)
	if m.connected:
		reply = m.get_config("running", ("subtree",filter))
		#print(reply)
		#print(reply.data)		

		tree_xml = etree.ElementTree(reply.data)
		print(etree.tostring(tree_xml))
if __name__ == '__main__':
    main()
