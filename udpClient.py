#/usr/bin/python
#UDP Client Script 
import socket

target_host = "localhost"
target_port = 9999 

#build socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect client
#client.connect((target_host, target_port))

#send some data
client.sendto("Hello, Kali!",(target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data

