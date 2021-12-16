import getpass
import sys
import telnetlib

#Enter your host IP to which you wish to telnet to instead of x.x.x.x
HOST = "10.197.174.195"

#The below command takes your username as input 
user = input("Enter your telnet username : ")

#This command is used to get your password
password = getpass.getpass()

#Executing the below command is similar to executing "telnet x.x.x.x" in command prompt, this command establishes the telnet session
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    
#the below commands will configure the loop back interface
tn.write(b"enable\n")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"sh ip int br \n")
print (tn.read_all())
