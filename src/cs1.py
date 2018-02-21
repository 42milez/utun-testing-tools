import socket
from datetime import datetime
from time import sleep
from contextlib import closing
import sys

host_name = sys.argv[1]
host_port = sys.argv[2]

#  Server Socket
# --------------------------------------------------

server_addr_v4 = '127.0.0.1'
server_port = '12345'
server_sock = socket.socket()
server_sock.bind((server_addr_v4, server_port))

#  Client Socket
# --------------------------------------------------

client_sock = socket.socket()
client_sock.connect((host_name, host_port))

# --------------------------------------------------

while True:
    print('listening...')
    server_sock.listen(5)
    c, addr = server_sock.accept()
    print('receiving')
    print(c.recv(4096))
    while True:
        print('sending')
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        try:
            c.send(now)
        except:
            break
        sleep(1)
    c.close()
    s.close()

