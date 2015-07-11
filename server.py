import socket

# create datagram socket
port = 5000
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(("", port))

connections = {}

# waiting on port
print("waiting on port %d" % port)
while 1:
    data, addr = soc.recvfrom(1024)

    print("data %s" % data)
    print("address %s" % str(addr))
    query = data.split()
    user = query[0]
    if user not in connections:
        connections[user] = addr
        print connections
    else:
        soc.sendto('hooo', connections[user])

    if data:
        soc.sendto("yahooo", addr)
        #soc.sendto(msg, addr)
    else:
        break
