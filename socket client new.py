import socket

host='localhost'
port=5000
s=socket.socket()
s.connect((host,port))

while True:
    x=input("Enter client message: ")
    y=x.encode()
    k=y.upper()
    s.send(k)
    data=s.recv(1024)
    z=data.decode()
    print(z)

    if(x=='bye'):
        break
