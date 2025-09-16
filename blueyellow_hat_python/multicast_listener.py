import socket 
import struct 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

s.bind(("", 2046)) # port to bind on any interface 

mreq = struct.pack("4s1", 
                   socket.inet_aton("234.0.0.2"), 
                   socket.INADDR_ANY) 
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq) 

while True: 
    data = s.recv(2048) 
    print(data) 
    # or 
    # open("file", "wb+")... write(data) 

