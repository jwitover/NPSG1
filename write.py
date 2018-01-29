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