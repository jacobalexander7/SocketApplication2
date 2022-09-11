# Jacob Coomer
# This server implements a basic protocol for sending messages over TCP/UDP. 
# The server can return: Client IP, Client Port, or a latency calculation.
# Python 3.9.7 | Dependencies: socket, argparse, datetime, time
# Command Line Instructions: 
# 1. Start the server application. Ex: python3 server.py -t TCP -p 8000
# 2. Start the client and supply connection information. Ex: python3 client.py -t TCP -i 127.0.0.1 -p 8000
# 3. Send a message from the client menu.
# Defaults: 
# Type = TCP
# Port = 8000

from socket import *
from udp_server import *
from tcp_server import *
import argparse

parser = argparse.ArgumentParser("Server Program", description="This progrma runs the server portion of the application.")
parser.add_argument('-p', dest='port', help='Sets the connection port', type=int)
parser.add_argument('-t', dest='type', help='Sets the connection type (TCP/UDP)', type=str)
args = parser.parse_args()
print(args.type)

serverPort = args.port if args.port else 8000

if args.type and args.type == 'UDP':
    server = UDPServer(serverPort)
else:
    server = TCPServer(serverPort)
