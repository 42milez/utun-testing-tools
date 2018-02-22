#!/usr/bin/env python3

import socket
import sys
from time import sleep

host_name = sys.argv[1]
host_port = int(sys.argv[2])

client_sock = socket.socket()
client_sock.connect((host_name, host_port))
print('Client connected to the host.')

client_sock.send(b"ping!")

try:
    while True:
        print('Recieved: ' + client_sock.recv(512).decode())
        client_sock.send(b"ping!")
        sleep(1)
except KeyboardInterrupt:
    client_sock.close()
