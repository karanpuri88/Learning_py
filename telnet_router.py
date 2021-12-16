import telnetlib

host = "10.197.174.195"

test = telnetlib.Telnet(host)

test.read_until(b"username:")

test.write(cisco + "/n")

test.read_until(b"password:")

test.write(cisco + "/n")

interface = test.write("sh ip int br" + "/n")

print (interface)
