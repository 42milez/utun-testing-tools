#!/usr/bin/env python3

import socket

server_addr_v4 = '127.0.0.1'
server_port = 12346
server_sock = socket.socket()
server_sock.bind((server_addr_v4, server_port))
server_sock.listen(5)
print('Server has started.')

try:
    while True:
        sock, addr = server_sock.accept()
        print('Received: ' + sock.recv(512).decode())
        sock.send(b"pong!")
except KeyboardInterrupt:
    server_sock.close()
