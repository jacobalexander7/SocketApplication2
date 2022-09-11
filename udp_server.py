from socket import *
from datetime import *
from time import sleep

class UDPServer:
    def __init__(self, port):
        self.port = port
        self.startup()
    def startup(self):
        serverSocket = socket(AF_INET,SOCK_DGRAM)
        serverSocket.bind(('',self.port))
        print ("The server is ready to receive")

        while True:
            message, clientAddress = serverSocket.recvfrom(2048) #Taking 2048 bytes
            decoded = message.decode()
            if decoded== 'IP':
                self.returnIP(serverSocket, clientAddress)
            elif decoded == 'PORT':
                self.returnPort(serverSocket, clientAddress)
            elif decoded[0:9] == 'TIMEDELAY': 
                self.returnTime(serverSocket, clientAddress, decoded)
            #modifiedMessage = message.decode().upper()  #Use the decode method to process as string
    
    def returnIP(self, socket, clientAddress):
        socket.sendto(clientAddress[0].encode(), clientAddress)

    def returnPort(self, socket, clientAddress):
        socket.sendto(str(clientAddress[1]).encode(), clientAddress)
    
    def returnTime(self, socket, clientAddress, message):
        print(message)
        sleep(1) #Confirming the time measurement is correct
        clientTime = datetime.strptime(message[9::],"%Y-%m-%d %H:%M:%S.%f")
        serverTime = datetime.utcnow()
        difference = str(serverTime - clientTime)
        difference = difference + ' ' + str(serverTime)
        socket.sendto(difference.encode(), clientAddress)

#sending info         
#serverSocket.sendto(modifiedMessage.encode(), clientAddress) #Re-encode the string as bytes

