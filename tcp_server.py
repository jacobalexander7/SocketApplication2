from socket import *
from datetime import *
from time import sleep

class TCPServer:
    def __init__(self, port):
        self.port = port
        self.startup()
    def startup(self):
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind(('',self.port))
        serverSocket.listen(1)
        print ("The server is ready to receive")
        connection, addr = serverSocket.accept() 

        while True:
            decoded = connection.recv(2048).decode()

            if decoded== 'IP':
                self.returnIP(connection, addr)
            elif decoded == 'PORT':
                self.returnPort(connection, addr)
            elif decoded[0:9] == 'TIMEDELAY': 
                self.returnTime(connection, addr, decoded)
    
    def returnIP(self, connection, clientAddress):
        connection.send(clientAddress[0].encode())

    def returnPort(self, connection, clientAddress):
        connection.send(str(clientAddress[1]).encode())
    
    def returnTime(self, connection, clientAddress, message):
        print(message)
        sleep(1) #Confirming the time measurement is correct
        clientTime = datetime.strptime(message[9::],"%Y-%m-%d %H:%M:%S.%f")
        serverTime = datetime.utcnow()
        difference = str(serverTime - clientTime)
        difference = difference + ' ' + str(serverTime)
        connection.send(difference.encode())

#sending info         
#serverSocket.sendto(modifiedMessage.encode(), clientAddress) #Re-encode the string as bytes

