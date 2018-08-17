#!/usr/bin/env python
'''
script for using show_lldp.xml and find print lldp neighbor parameters:

{'fe-0/0/7.0': {'remote_port': '24', 'remote_sys_name': 'twb-sf-hpsw1'}}


'''
from __future__ import unicode_literals, print_function
from lxml import etree
from pprint import pprint

with open('show_lldp.xml') as f:
    lldp = etree.fromstring(f.read())

print()
print("Print XML Tree out as a string:")
print("-" * 20)
print(etree.tostring(lldp, pretty_print=True).decode())

print('\n\n')
print("Print one child element of the root element:")
print("-" * 20)
lldp_child = lldp.getchildren()[0]
print(lldp_child.tag)

for child in lldp_child:
    if child.tag == 'lldp-local-interface':
        local_intf = child.text
    elif child.tag == 'lldp-remote-system-name':
        remote_sys_name = child.text
    elif child.tag == 'lldp-remote-port-description':
        remote_port = child.text

lldp_dict = {
    local_intf: {
        'remote_sys_name': remote_sys_name,
        'remote_port': remote_port,
    }
}

print('\n\n')
print("Parse the returned data and create a dictionary.")
print("-" * 20)
pprint(lldp_dict)
print('\n\n')