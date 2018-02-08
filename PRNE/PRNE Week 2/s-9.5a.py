# from pprint import pprint
# import re
# 
# # Create regular expression to match Gigabit interface names
# gig_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9])')
# 
# routes = {}
# 
# # Read all lines of IP routing information
# file = open('ip-routes','r')
# for line in file:
#     match = gig_pattern.search( line ) # Match for Gigabit Ethernet
# 
#     # Check to see if we matched the Gig Ethernet string
#     if match:
#         intf = match.group(2) # get the interface from the match
#         routes[intf] = routes[intf]+1 if intf in routes else 1
# 
# print ''
# print 'Number of routes per interface'
# print '------------------------------'
# pprint(routes)
# print '' # Print final blank line
# 
####################################################
# 
# from pprint import pprint
# 
# # Print heading
# print ''
# print 'Counts of different OS-types for all devices'
# print '============================================'
# 
# os_types = { 'Cisco IOS':    {'count':0, 'devs':[] },
#              'Cisco Nexus':  {'count':0, 'devs':[] },
#              'Cisco IOS-XR': {'count':0, 'devs':[] },
#              'Cisco IOS-XE': {'count':0, 'devs':[] } }
# 			
# # Read all lines of device information from file
# file = open('devices','r')
# for line in file:
# 
#     device_info_list = line.strip().split(',') # Get device info into list
# 	
#     # Put device information into dictionary for this one device
#     device_info = {} # Create a dictionary of device info
#     device_info['name'] = device_info_list[0]
#     device_info['os-type'] = device_info_list[1]
# 
#     name = device_info['name'] # get the device name
#     os = device_info['os-type'] # get the OS-type for comparisons
# 	
# 	# Put device information into dictionary for this one device
#     device_info = {} # Create a dictionary of device info
#     device_info['name'] = device_info_list[0]
#     device_info['os-type'] = device_info_list[1]
# 
#     name = device_info['name'] # get the device name
#     os = device_info['os-type'] # get the OS-type for comparisons
# 	
# 	# Based on the OS-type, increment the count and add name to list
#     if os == 'ios':
#         os_types['Cisco IOS']['count'] += 1
#         os_types['Cisco IOS']['devs'].append(name)
# 
#     elif os == 'nx-os':
#         os_types['Cisco Nexus']['count'] += 1
#         os_types['Cisco Nexus']['devs'].append(name)
# 
#     elif os == 'ios-xr':
#         os_types['Cisco IOS-XR']['count'] += 1
#         os_types['Cisco IOS-XR']['devs'].append(name)
# 
#     elif os == 'ios-xe':
#         os_types['Cisco IOS-XE']['count'] += 1
#         os_types['Cisco IOS-XE']['devs'].append(name)
# 
#     else:
#         print "   Warning: unknown device type:", os
# 		
# pprint(os_types)
# print '' # Print final blank line
# 
# file.close() # Close the file since we are done with it
# 
###############################################################

import pexpect
from pprint import pprint
import re

# Print heading
print ''
print 'Interfaces, routes list, routes details'
print '---------------------------------------'

# Create regular expressions to match interfaces and OSPF
OSPF_pattern = re.compile('^O')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9])')

# Create regular expressions to match prefix and routes
prefix_pattern = re.compile('^O.{8}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# Connect to device and run 'show ip route' command
print '--- connecting telnet 10.30.30.1 with cisco/cisco'

session = pexpect.spawn('telnet 10.30.30.1', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print 'Timeout or unexpected reply from device'
    exit()

# Successfully got username prompt, enter username
session.sendline('cisco')
result = session.expect('Password:')

# Enter password
session.sendline('cisco')
result = session.expect('>')

# Must set terminal length to zero for long replies
print '--- setting terminal length to 0'
session.sendline('terminal length 0')
result = session.expect('>')

# Run the 'show ip route' commanmd on device
print '--- successfully logged into device, performing show ip route command'
session.sendline('show ip route')
result = session.expect('>')

# Print out the output of the command, for comparison
print '--- show ip route output:'
show_ip_route_output = session.before
print show_ip_route_output

# Get the output from the command into a list of lines from the output
routes_list = show_ip_route_output.splitlines()

intf_routes = {} # Create dictionary to hold number of routes per interface

# Go through the list of routes to get routes per interface
for route in routes_list:

    OSPF_match = OSPF_pattern.search(route)
    if OSPF_match:
        intf_match = intf_pattern.search( route ) # Match for Gigabit Ethernet
        # Check to see if we matched the Gig Ethernet string
        if intf_match:
            intf = intf_match.group(2) # get the interface from the match
            if intf not in intf_routes: # If route list not yet created, do so now
                intf_routes[intf] = []

            # Extract the prefix (destination IP address/subnet)
            prefix_match = prefix_pattern.search(route)
            prefix = prefix_match.group(1)

            # Extract the route
            route_match = route_pattern.search(route)
            next_hop = route_match.group(1)

            # Create dictionary for this route, and add it to the list
            route = {'prefix':prefix,'next-hop':next_hop}
            intf_routes[intf].append(route)

pprint(intf_routes)
print '' # Print final blank line
