import pexpect

# Define variables for your IP address, username, and password 

ip_address = '10.30.30.1'
username = 'cisco'
password = 'cisco'

# Create the pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! creating session for: ', ip_address
    exit()

# Session expecting username, enter it here
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! entering username: ', username
    exit()

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' FAILURE! entering password: ', password
    exit()

# Print a success message if the login completes successfully. Close the Telnet session.

print '--- Success! connecting to: ', ip_address
print '---               Username: ', username
print '---               Password: ', password
print '------------------------------------------------------\n'

# Terminate telnet to device and close pexpect session
session.sendline('quit')
session.close()
