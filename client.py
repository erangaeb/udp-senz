import socket
import sys

host = "10.2.2.132"
port = 5000

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    # send data to server
    msg = raw_input("Enter message: ")
    soc.sendto(msg, (host, port))

    # recv data from client
    data, addr = soc.recvfrom(1024)
    print("reply: %s" %data)
