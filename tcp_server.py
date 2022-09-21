from socket import *
from datetime import *
from time import sleep

#This class controls the TCP server methods.
#There are slight variations between sending with UDP/TCP, so I split them into classes.
class TCPServer:
    
    def returnIP(self, connection, clientAddress):
        connection.send((str(clientAddress[0])+' OK').encode())

    def returnPort(self, connection, clientAddress):
        connection.send((str(clientAddress[1])+' OK').encode())
    
    def returnTime(self, connection, clientAddress, message):
        print(message)

        clientTime = datetime.strptime(message[9::],"%Y-%m-%d %H:%M:%S.%f")
        serverTime = datetime.utcnow()

        sleep(1) #Confirming the time measurement is correct

        difference = str(serverTime - clientTime)  #Calculating time delay
        difference = difference + ' ' + str(serverTime)
        difference = difference + ' OK'
        connection.send(difference.encode())

    def returnInvalid(self, connection, clientAddress):
        connection.send('INVALID'.encode())