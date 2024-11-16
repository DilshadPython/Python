import socket

# create a call throw socket
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make a connect
my_sock.connect(('data.pr4e.org', 80))
# get request the data from the url 
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

my_sock.close()
