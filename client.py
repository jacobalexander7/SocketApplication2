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

#Handling Command Line Parameters
parser = argparse.ArgumentParser("Client Program", description="Runs the client portion of the program.")
parser.add_argument('-i', dest='ip', help='Sets the IP for the connection', type=str, default = '127.0.0.1')
parser.add_argument('-p', dest='port', help='Sets the PORT for the connection', type=int, default = 8000)
parser.add_argument('-t', dest='type', help="Sets the TYPE for the connection (TCP/UDP)", type=str, default = 'tcp')
args = parser.parse_args()

def showMenu():  #Client menu
    print("Client started.\nEnter a number.\n1. IP\n2. PORT\n3. TIMEDELAY\n4. QUIT.\n")

if args.type == 'UDP':  #Create object based on UDP or TCP input
    client = UDPClient(args.ip,args.port)
    connection = socket(AF_INET, SOCK_DGRAM)

else:
    client = TCPClient()
    connection = socket(AF_INET, SOCK_STREAM)
    connection.connect((args.ip,args.port))

showMenu()
#Main Loop for client
while True:  
        message = input('\nEnter the number for a command: ')
        client.send(connection, message)
