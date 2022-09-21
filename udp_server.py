from socket import *
from datetime import *
from time import sleep

#This class controls the UDP server methods.
#There are slight variations between sending with UDP/TCP, so I split them into classes. 
class UDPServer:
    
    def returnIP(self, connection, clientAddress):
        connection.sendto((clientAddress[0]+' OK').encode(), clientAddress)

    def returnPort(self, connection, clientAddress):
        connection.sendto((str(clientAddress[1])+' OK').encode(), clientAddress)
    
    def returnTime(self, connection, clientAddress, message):
        print(message)

        clientTime = datetime.strptime(message[9::],"%Y-%m-%d %H:%M:%S.%f")
        serverTime = datetime.utcnow()
        
        sleep(1) #Confirming the time measurement is correct

        difference = str(serverTime - clientTime)
        difference = difference + ' ' + str(serverTime)
        difference = difference + ' OK'
        connection.sendto(difference.encode(), clientAddress)

    def returnInvalid(self, connection, clientAddress):
        connection.sendto('INVALID'.encode(), clientAddress)