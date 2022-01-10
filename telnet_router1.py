# https://docs.python.org/3/library/telnetlib.html#telnetlib.Telnet

import telnetlib

# Enter Router IP address 
host= input ("Enter the IP address of Router : ")

# Creating Session to telnet to router Telnet is function inside telnetlib (module.function())
session = telnetlib.Telnet(host)

# Enter Username & Password
user = input("Enter Username :")
pas = input("Enter Password :")

# Default string is UTF-8 convert into ascii becuase telnet uses byte strings
username = user.encode("ascii")
password = pas.encode("ascii")

# Read untill username & password in byteString & then write  
session.read_until(b"Username:")
session.write(username + b"\n")
session.read_until(b"Password:")
session.write(password + b"\n")

# Enter the command to read from router 
com = input("Enter the read command to you want to run :")
command = com.encode("ascii")
session.write(command + b"\n")

#Read the output & convert into UTF-8 Format otherwise output would be in bytes ascii format & very clumpsy 
out = session.read_all()
output = out.decode("utf-8")
print(output)

# Close Telnet session
session.close()

