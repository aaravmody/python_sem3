import socket
host='localhost'
port=5000
s=socket.socket()
s.connect((host,port))
message=s.recv(1024)
while message:
    print(message.decode())
    message=s.recv(1024)
s.close
