import pexpect
import re
routes_list = [] # Create the list of routes


#-----------------------------------------------------------
# The following code connects to a device and dumps all
# routing information

print '--- connecting telnet 10.30.30.1 with cisco/cisco'

session = pexpect.spawn('telnet 10.30.30.1', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print 'Timout or unexpected reply from device'
    exit()

# Successfully got password prompt, logging in with username
session.sendline('cisco')
result = session.expect('Password:')

# Successfully got password prompt, logging in with username
session.sendline('cisco')
result = session.expect('>')

# Must set terminal length to zero for long replies
print '--- setting terminal length to 0'
session.sendline('terminal length 0')
result = session.expect('>')

# Execute the 'show ip route' command to get routing info
print '--- executing: show ip route'
session.sendline('show ip route')
result = session.expect('>')

# Get output from ip route command
print '--- getting ip route command output'
show_ip_route_output = session.before

print ''
print 'IP route output'
print '----------------------------------------------------'
print show_ip_route_output
print '----------------------------------------------------'
print ''

# Get routing information into list
routes_list = show_ip_route_output.splitlines()

while True: # Loop forever, until user terminates program

    # Request user to input the IP destination route prefix we will search for
    try:
        ip_address = raw_input('Enter IP destination address to find (Ctrl-C to exit):')
    except KeyboardInterrupt:
        break;
		
	# Set the pattern for matching OSPF routes
    route_pattern = re.compile('^O.{8}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

    # Loop through our devices looking for a match on IP address
    for route in routes_list:

        # Search for our route string, and continue to next iteration if not found
        route_match = route_pattern.search(route)
        if not route_match: continue

        # Found our IP address, print out route information
        if route_match.group(1) == ip_address:
            route_info = route.split(',')
            print '  ---- Route:     ', route_info[0][5:].strip()
            print '  ---- Time:      ', route_info[1].strip()
            print '  ---- Interface: ', route_info[2].strip()
            print ''
            break

    else:  # We get here if we exhausted the device list, IP not found
        print '--- Given route prefix not found ---'

print '\n'
print 'Route search terminated.\n'

session.sendline('quit')
session.kill(0)