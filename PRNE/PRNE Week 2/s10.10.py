# devices_list = [] # Create the outer list for all devices
# 
# # Read in the devices from the file
# file = open('devices','r')
# for line in file:
# 
#     device_info_list = line.split(',') # Get device info into list
#     devices_list.append(device_info_list)
# 
# file.close() # Close the file since we are done with it
# 
# print ''
# print 'Name     OS-type    IP address           Software            '
# print '-------  ---------  -------------------  --------------------'
# 
# ip_addresses = set()
# 
# # Go through the list of devices, printing out values in nice format
# for device in devices_list:
# 
#     print '{0:8} {1:10} {2:20} {3:20}'.format(device[0],device[1],device[2],device[3]),
# 
#     # Print 'duplicate' if IP address exists for another device
#     if device[2] in ip_addresses:
#         print '*Duplicate IP!*'
#         continue
# 
#     ip_addresses.add(device[2])
#     print ''
# 
# print '' 
# 
#################################################

devices_list = [] # Create the outer list for all devices

print ''
print 'Idx Name     OS-type  IP address           Software            '
print '--- -------- -------- -------------------- --------------------'

index = 0

# Read in the devices from the file
file = open('devices','r')
for line in file:

    device_info = line.split(',') # Get device info into list
    devices_list.append(device_info)

    print '{0:2}: {1:8} {2:8} {3:20} {4:20}'.format(index+1,
                                                    device_info[0],device_info[1],
                                                    device_info[2],device_info[3])

    index += 1 # increment our index

file.close() # Close the file since we are done with it
print ''
while True: # Loop forever, until user terminates program

    # Request user to input the IP address we will search for
    try:
        ip_address = raw_input('Enter device IP address to find (Ctrl-C to exit):')
    except KeyboardInterrupt:
        break;

    # Loop through our devices looking for a match on IP address
    for index in range(0, len(devices_list)):

        device_info = devices_list[index] # Get information for this device in the list
        if device_info[2][5:] == ip_address:  # Check to see if device IP is a match

            # If a match, print results and stop looking
            print '{0:2}: {1:8} {2:8} {3:20} {4:20}'.format(index+1,
                                                     device_info[0],device_info[1],
                                                     device_info[2],device_info[3])
            break
        else:
            continue

    else:  # We get here if we exhausted the device list, IP not found
        print '--- Given IP address not found ---'

print '\n'
print 'Device search terminated.\n' 