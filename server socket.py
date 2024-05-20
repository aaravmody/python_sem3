import socket
host='localhost'
port=5000
s=socket.socket()
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
print("gotcha",addr)
c.send(b"bheja")
c.close()
