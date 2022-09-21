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
from datetime import *
import argparse

parser = argparse.ArgumentParser("Server Program", description="This progrma runs the server portion of the application.")
parser.add_argument('-p', dest='port', help='Sets the connection port', type=int, default='8000')
parser.add_argument('-t', dest='type', help='Sets the connection type (TCP/UDP)', type=str)
args = parser.parse_args()
print(args.type)

#Reusable logging method
def createLog(logFile, method):
    validMethods = ('IP', 'PORT', 'TIMEDELAY')
    current = '/'.join(str(datetime.utcnow()).split(' '))
    response = 'OK' if method[0:9] in validMethods else 'INVALID'

    log = ("{} {} {}\n").format(current, method, response)
    logFile.write(log)
    
logFile = open('logs.txt', 'a')

if args.type == 'UDP':  #Create object based on command line flag
    server = UDPServer()
    connection = socket(AF_INET,SOCK_DGRAM)
    connection.bind(('',args.port))

else:
    server = TCPServer()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',args.port))
    serverSocket.listen(1)
    connection, addr = serverSocket.accept() 

print("The server is ready to receive")
#Main server loop. Used to check for valid methods and create logs.
while True:
    if type(server) == UDPServer:
        message, addr = connection.recvfrom(2048)
        decoded = message.decode()
    else:
        decoded = connection.recv(2048).decode()

    if decoded == 'IP':
        server.returnIP(connection, addr)

    elif decoded == 'PORT':
        server.returnPort(connection, addr)

    elif decoded[0:9] == 'TIMEDELAY': #Use try to check for bad datetime object
        try: 
            server.returnTime(connection, addr, decoded)
        except:
            server.returnInvalid(connection, addr)
        
    else:
        server.returnInvalid(connection, addr)
    
    createLog(logFile, decoded)
