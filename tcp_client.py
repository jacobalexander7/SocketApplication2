from socket import *
from datetime import * 

#This object controls the TCP Client methods.
#There are slight variations between sending with UDP/TCP, so I split them into classes.

class TCPClient():

    def receiveMessage(self, client):
        modifiedMessage, serverAddress = client.recvfrom(2048)
        print(modifiedMessage.decode())

    def send(self, client, message):
        print(message)
        if message == "1":
            client.send('IP'.encode())
            self.receiveMessage(client)

        elif message == "2":
            client.send('PORT'.encode())
            self.receiveMessage(client)

        elif message == "3":
            current = 'TIMEDELAY' + str(datetime.utcnow())
            client.send(str(current).encode())

            modifiedMessage, serverAddress = client.recvfrom(2048)
            splitMessage = modifiedMessage.decode().split(' ')
            
            print('Delay SENDING: ' + splitMessage[0])  #Calculating time delay
            convertedServerTime = datetime.strptime(splitMessage[1]+' '+splitMessage[2],"%Y-%m-%d %H:%M:%S.%f")
            totalDelay = str(datetime.utcnow() - convertedServerTime)
            print('Delay RECEIVING: ' + totalDelay)

        elif message == '4':
            client.close()
            print("Exiting the client.")
            exit()
            
        else:
            client.send(message.encode())
            self.receiveMessage(client)
        # else:
        #     print('Invalid selection.')
