file = open('dev-01-info', 'r')

name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

print '--- Device info nicely formatted ----------------------------------'
print 'Name     IP addr         OS       Username   Password'
print '-----    --------------- -----    --------   --------'
print '{0:8} {1:15} {2:8} {3:10} {4:10}'.format(name, ip_address, os_type,username, password)
print '-------------------------------------------------------------------'

# Create comma-separated list of device information attributes
device_info = name                             # start with device name
device_info = device_info + ',' + ip_address   # add a comma and IP address
device_info = device_info + ',' + os_type      # add a comma and os-type
device_info = device_info + ',' + username     # add a comma and username
device_info = device_info + ',' + password     # add a comma and password

# Write device information line to file
print '--- Writing device information to file ----------------------------'
outfile = open('dev-info-out','w')   # open the output file
outfile.write(device_info)           # write the line of device information
outfile.write('\n')                  # with 'write' we must add ending newline char
outfile.close()                      # close file when writing is complete

