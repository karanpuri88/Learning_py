import netmiko

# Take all inputs from User 
ip_address = input("Enter IP address")
user = input("Enter Username :")
pas = input("Enter Password :")

# Device type is important while using connecthandler function of netmiko as it support multivendor
session = netmiko.ConnectHandler(ip = ip_address, username = user, password = pas, device_type = "cisco_xe")

# Enter command to run & print it 
command = input("Enter Command to run")
print(session.send_command(command + "\n"))

#Disconnect Session
session.disconnect()
