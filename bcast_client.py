import socket
import sys

host = "10.2.2.132"
port = 5000

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((host, port))

while 1:
    # recv data from client
    data, addr = soc.recvfrom(1024)
    print("data: %s" %data)
