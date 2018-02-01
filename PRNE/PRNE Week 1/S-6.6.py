import pexpect

ip_address = '10.30.30.1'
username = 'cisco'
password = 'cisco'
password_enable = 'cisco'

#create the pexpect session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! creating session for: ', ip_address
    exit()

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' FAILURE! entering password: ', password
    exit()


# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' Failure! entering enable mode'
    exit()

# Send enable password
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' Failure! entering enable mode after sending password'
    exit()

# Issue config t command.  
session.sendline('config t')
result = session.expect(['r1\(config\)#', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' Failure! entering config mode'
    exit()

# Change the hostname to R1
session.sendline('hostname R1')
result = session.expect(['R1\(config\)#', pexpect.TIMEOUT])