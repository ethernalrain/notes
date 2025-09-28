#
# Key generation:
#
# openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt
#
# openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt
#
#

import socket
import ssl

client_key = "client.key"
client_cert = "client.crt"
server_cert = "server.crt"

port = 8080
hostname = '127.0.0.1'

context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)
context.load_verify_locations(cafile=server_cert)

context.verity_mode = ssl.CERT_REQUIRED
context.options |= ssl.OP_SINGLE_ECDH_USE

with socket.create_connection((hostname, port)) as sock:

	with context.wrap_socket(sock, server_side=False, server_hostname=hostname) as s:

		# use s as a regular socket then

		print(s.version())

		s.send("aaaa".encode())
		data = s.recv(1024).decode()
		print(data)


