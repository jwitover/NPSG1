current_version = 'Version 5.3.1'

file = open('devices' , 'r')

print ''
print '      Devices NOT running Version 5.3.1 '
print '      =========================================='

for line in file:
    device_info_list = line.strip().split(',')

    device_info = {}
    device_info['name'] = device_info_list[0]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]
	
    if device_info['version'] != current_version:
        print '      Device:', device_info['name'], '   Version:', device_info['version']
	
print '' 

file.close()

#import re
#
#print ''
#print 'Devices and their Management IP addreses'
#print '========================================'
#
#ip_addr_pattern = re.compile('Mgmt:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
#
#file = open('devices', 'r')
#
#for line in file:
#    device_info_list = line.strip().split(',')
#    device_info = {}
#    device_info['name'] = device_info_list[0]
#    mgmt_addr = ip_addr_pattern.search(line)
#    device_info['ip'] = mgmt_addr.group(1)
#	
#    print '   Device:', device_info['name'], '   Mgmt IP:', device_info['ip']
#print '========================================'	
#print ''
#
#file.close()
