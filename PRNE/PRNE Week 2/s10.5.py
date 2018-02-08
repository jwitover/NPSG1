# devices_list = [] # Create the outer list for all devices
# 
# # Read in the devices from the file
# file = open('devices','r')
# for line in file:
# 
#     device_info_list = line.strip().split(',') # Get device info into list
#     devices_list.append(device_info_list)
# 
# file.close() # Close the file since we are done with it
# 
# print ''
# print 'Name     OS-type  IP address           Software         '
# print '------   -------  ------------------   ------------------'
# 
# # Go through the list of devices, printing out values in nice format
# for device in devices_list:
# 
#     print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
#                                              device[2],device[3])
# 
# print ''

devices_list = [] # Create the outer list for all devices

file = open('devices','r')
line = file.readline()
while line:

    device_info_list = line.strip().split(',') # Get device info into list

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]

    # Now append our device and its info onto our 'devices' list
    devices_list.append(device_info)

    line = file.readline()

file.close() # Close the file since we are done with it

# Use while loop to print the results
print ''
print 'Name     OS-type  IP address           Software         '
print '------   -------  ------------------   ------------------'

index = 0
while index < len(devices_list):

    device = devices_list[index]

    print '{0:8} {1:8} {2:20} {3:20}'.format(device['name'],
                                             device['os-type'],
                                             device['ip'],
                                             device['version'])

    index += 1

print ''