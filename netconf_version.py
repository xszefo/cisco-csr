#!/usr/bin/python3

#import ncclient.manager

from ncclient import manager
from lxml import etree

host = 'ios-xe-mgmt.cisco.com'
port = '10000'
username = 'developer'
password = 'C1sco12345'

print(f'Connecting to {host}...')
filter ="""
	<native>
		<version>
		</version>
	</native>
"""
print(filter)
m = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False)
if m.connected:
	reply = m.get_config("running", ("subtree",filter))

	tree_xml = etree.ElementTree(reply.data)
	
	root = tree_xml.getroot()

	#for elem in root.iter():
	#	print(tree_xml.getelementpath(elem))
	
	ver1 = root.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}native/{http://cisco.com/ns/yang/Cisco-IOS-XE-native}version').text
	ver2 = root.find('{*}native/{*}version').text	
	print(f'{ver1}\n{ver2}')	
	for i in root.iter('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}version'):
		print(i.text)
    
	m.close_session()

