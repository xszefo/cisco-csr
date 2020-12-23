#!/usr/bin/python3

import ncclient.manager
from lxml import etree

host = 'ios-xe-mgmt.cisco.com'
port = '10000'
username = 'developer'
password = 'C1sco12345'

print(f'Connecting to {host}...')
filter ="""
	<native>
		<hostname>
		</hostname>
	</native>
"""
print(filter)
m = ncclient.manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False)
if m.connected:
	reply = m.get_config("running", ("subtree",filter))

	tree_xml = etree.ElementTree(reply.data)
	
	root = tree_xml.getroot()

	hostname = root.find('{*}native/{*}hostname').text	
	print(hostname)

	m.close_session()
