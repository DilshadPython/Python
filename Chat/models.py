import socket
from threading import Thread

# server IP address

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7002
# This will use to separate the client name and hist message
separator_token = "<SEP>" 

# initialize list/set of all connect client's socket
client_sockets = set()