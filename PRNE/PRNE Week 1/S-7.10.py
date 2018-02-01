from pprint import pprint

# -----------------------------------
# 
# file = open('devices','r')
# file_line = file.readline().strip()
# 
# device_info = file_line.split(',')
# 
# pprint(device_info) # Print the dictionary with nice formatting
# 
# file.close()
# 
#---------------------------------

#---------------------------------

# file = open('devices','r')
# file_line = file.readline().strip()
# 
# device_info_list = file_line.split(',')
# 
# device_info = {}  # Create my device_info dictionary
# device_info['name'] = device_info_list[0]
# device_info['os-type'] = device_info_list[1]
# device_info['ip'] = device_info_list[2]
# device_info['username'] = device_info_list[3]
# device_info['password'] = device_info_list[4]
# 
# pprint(device_info) # Print the dictionary with nice formatting
# 
# file.close()

#---------------------------------

#---------------------------------

devices = [] # Create the outer list for all devices 

file = open('devices', 'r')
# device_info = {}
for line in file:
    device_info_list = line.strip().split(',')
	
    device_info = {}  # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]
    devices.append(device_info)

pprint(devices)

file.close()

#---------------------------------

#---------------------------------

# devices = {} # Create the outer dictionary for all devices
# 
# file = open('devices','r')
# for line in file:
# 
#     device_info_list = line.strip().split(',') # Get device info into list
# 
#     # Put device information into dictionary for this one device
#     device_info = {} # Create the inner dictionary for device info
#     device_info['name'] = device_info_list[0]
#     device_info['os-type'] = device_info_list[1]
#     device_info['ip'] = device_info_list[2]
#     device_info['username'] = device_info_list[3]
#     device_info['password'] = device_info_list[4]
# 
#     # Print out what we have read and built so far
#     print 'device_info: ', device_info
# 
#     # Now place our device and its info onto our 'devices' dictionary
#     devices[device_info['name']] = (device_info)
# 
# # Done with all lines in the file; now print the results
# pprint(devices)
# 
# file.close()

#---------------------------------

#---------------------------------

# For simplicity we will create our outer dictionary and lists
# devices = {} # Create the outer dictionary for all OS-types
# devices['ios'] = []     # Create initial empty list of devices
# devices['nx-os'] = []   # Create initial empty list of devices
# devices['ios-xr'] = []  # Create initial empty list of devices
# 
# file = open('devices','r')
# for line in file:
# 
#     device_info_list = line.strip().split(',') # Get device info into list
# 
#     # Put device information into dictionary for this one device
#     device_info = {} # Create the inner dictionary for device info
#     device_info['name'] = device_info_list[0]
#     device_info['os-type'] = device_info_list[1]
#     device_info['ip'] = device_info_list[2]
#     device_info['username'] = device_info_list[3]
#     device_info['password'] = device_info_list[4]
# 
#     # Print out what we have read and built so far
#     print 'device_info: ', device_info
# 
#     # Now place our device and its info onto the correct list of devices,
#     # , in our main OS-type dictionary, based on the device's OS-type.
#     devices[device_info['os-type']].append(device_info)
# 
# # Done with all lines in the file; now print the results
# pprint(devices)
# 
# file.close() # Close the file since we are done with it