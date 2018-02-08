class NetworkDevice():

    def set_info(self, name, os, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.os_type    = os
        self.username = user
        self.password = pw


#---- Function to go through devices printing them to table -----------
def print_device_info(devices_list):

    print ''
    print 'Name        OS-type  IP address   Username  Password'
    print '---------   -------  ----------   --------  --------'

    # Go through the list of devices, printing out values in nice format
    for device in devices_list:

        print '{0:11} {1:8} {2:12} {3:9} {4:9}'.format(device.name,
                                                       device.os_type,
                                                       device.ip_address,
                                                       device.username,
                                                       device.password)

    print ''
	
#---- Main: read device info, then print ------------------------------

dev1 = NetworkDevice()
dev1.set_info('dev1','IOS-NX','9.9.9.9')

dev2 = NetworkDevice()
dev2.set_info('dev2','IOS-XE','8.8.8.8','chuck','secret')

print_device_info([dev1,dev2])

#---- Class to hold information about a network device ----------------
class NetworkDevice():

    def __init__(self, name, ip, os, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.os_type    = os
        self.username = user
        self.password = pw
		
#---- Function to read device information from file -------------------
def read_device_info(devices_file):

    devices = [] # Create a list for all devices

    # Read in the devices from the file
    file = open(devices_file,'r')
    for line in file:

        device_info = line.strip().split(',') # Get device info into list

        # Create a device object with this data
        device = NetworkDevice(device_info[0],device_info[2],
                               device_info[1],device_info[3],device_info[4])

        devices.append(device) # add this device object to list

    file.close() # Close the file since we are done with it

    return devices # return a reference to the list we created
	
#---- Function to go through devices printing them to table -----------
def print_device_info(devices_list):

    print ''
    print 'Name        OS-type  IP address       Username  Password'
    print '---------   -------  --------------   --------  --------'

    # Go through the list of devices, printing out values in nice format
    for device in devices_list:

        print '{0:11} {1:8} {2:16} {3:9} {4:9}'.format(device.name,
                                                       device.os_type,
                                                       device.ip_address,
                                                       device.username,
                                                       device.password)

    print ''

#---- Main: read device info, then print ------------------------------

devices_list = read_device_info('devices')
print_device_info(devices_list)

devices_list = read_device_info('real-devices')
print_device_info(devices_list)