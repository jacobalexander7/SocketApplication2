# Jacob Coomer
# This client implements a basic protocol for sending messages over TCP/UDP. 
# The server can return: Client IP, Client Port, or a latency calculation.
# Python 3.9.7 | Dependencies: socket, argparse, datetime, time
# Command Line Instructions: 
# 1. Start the server application. Ex: python3 server.py -t TCP -p 8000
# 2. Start the client and supply connection information. Ex: python3 client.py -t TCP -i 127.0.0.1 -p 8000
# 3. Send a message from the client menu.
# Defaults: 
# Type = TCP
# IP = 127.0.0.1
# Port = 8000

from socket import *
import argparse
from udp_client import *
from tcp_client import *

parser = argparse.ArgumentParser("Client Program", description="Runs the client portion of the program.")
parser.add_argument('-i', dest='ip', help='Sets the IP for the connection', type=str)
parser.add_argument('-p', dest='port', help='Sets the PORT for the connection', type=int)
parser.add_argument('-t', dest='type', help="Sets the TYPE for the connection (TCP/UDP)", type=str)
args = parser.parse_args()

serverIP = args.ip if args.ip != None else '127.0.0.1'
serverPort = args.port if args.port != None else 8000

if args.type and args.type == 'UDP':
    client = UDPClient(serverIP, serverPort)
else:
    client = TCPClient(serverIP, serverPort)
#clientSocket.close  close udp