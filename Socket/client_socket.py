import socket

'''
we have to run the server we created python server.py and open new terminal tab
run python client_server.py 
created readme.txt file in current folder where the two server are runing
'''

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('127.0.0.1',8001))
cmd = 'GET http://127.0.0.1/readne.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

my_sock.close()
