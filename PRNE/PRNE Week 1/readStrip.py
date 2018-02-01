# Read in the device information
file = open('dev-01-info','r')

#Read in the device information one line at a time

name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

# print out the information

print 'device name: ',name
print 'ip address:  ',ip_address
print 'os type:     ',os_type
print 'username:    ',username
print 'password:    ',password