#---------------------------------

#---------------------------------
# Create a Tuple to Hold Device Information
# Use device

# from pprint import pprint
# 
# # Open the file and read in the single line of device info
# file = open('devices','r')
# file_line = file.readline().strip()
# 
# print 'read line: ', file_line # Print out the line I just read
# 
# # 'split()' will provide is with a python list, which we convert to a tuple
# device_info = tuple(file_line.split(','))
# 
# pprint(device_info) # Print out the tuple with nice formatting
# 
# file.close() 
# 
# #---------------------------------
# 
# #---------------------------------
# # Create a List of Tuples to Hold Device Information About Multiple Devices
# # Use device3
# 
# from pprint import pprint
# 
# devices = [] # Create the outer list for all devices
# 
# file = open('devices','r')
# for line in file:
# 
#     device_info = tuple(line.strip().split(',')) # Get device info into tuple
# 
#     # Print out what we have read and built so far
#     print 'device_info: ', device_info
# 
#     # Now append our device and its info onto our 'devices' list
#     devices.append(device_info)
# 
# # Done with all lines in the file; now print the results
# 
# pprint(devices)
# 
# file.close() 
# 
# #---------------------------------
# 
# #---------------------------------
# #Create a Dictionary of Named Tuples Which Hold Device Information
# # use devices3
# 
# from collections import namedtuple
# from pprint import pprint
# 
# Dev_info = namedtuple('Dev_info',['name', 'os', 'ip', 'user', 'password'])
# 
# devices = {}
# 
# file = open('devices','r')
# for line in file:
#     device_info = Dev_info(*(line.strip().split(',')))
#     print 'Device Information: ', device_info
#     devices[device_info.name] = device_info
# 
# pprint(devices)
# file.close()
# 
# #---------------------------------
# 
# #---------------------------------
# # Create a Set of All the OS Types Present for the List of Devices Read from a File
# # use device3
# 
# from collections import namedtuple
# from pprint import pprint
# 
# Dev_info = namedtuple('Dev_info',['name', 'os_type', 'ip', 'user', 'password'])
# 
# os_types = set()
# 
# file = open('devices','r')
# for line in file:
# 
#     device_info = Dev_info(*(line.strip().split(',')))
#     print 'Device Information: ', device_info
# 
#     if device_info.os_type not in os_types:
#         os_types.add(device_info.os_type)
# 
# pprint(os_types)
# file.close()


