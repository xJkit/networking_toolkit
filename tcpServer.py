#/usr/bin/python
#make your own TCP Server
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5) #limit: 5 connections

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# handle client's thread
def handle_client(client_socket):

    #show the data sent from clients
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # respond a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # activate our client thread to handle the incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
