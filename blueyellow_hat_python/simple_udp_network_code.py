import socket 

buffer = "...."

s = socket.socket(socket.AF_INET,
				socket.SOCK_DGRAM)
s.sendto(buffer, ('192.168.0.1', 69))

resp = s.recvfrom(2048)

