import socket

host='localhost'
port=5000
s=socket.socket()
s.bind((host,port))
s.listen()
conn,addr=s.accept()
while True:
    x=conn.recv(1024).decode()
    print(x)
    if x=='bye':
        break
    y=input("Enter data: ")
    data=y.encode()
    conn.send(data)
conn.close()
    
