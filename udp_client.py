from socket import *
from datetime import * 

#This class controls the UDP Client methods.
class UDPClient():
    def __init__(self, serverIP, serverPort) -> None:
        self.serverInfo = (serverIP, serverPort)
        
    def receiveMessage(self, client):
        modifiedMessage, serverAddress = client.recvfrom(2048)
        print(modifiedMessage.decode())

    def send(self, client, message):
        print(message)
        if message == "1":
            client.sendto('IP'.encode(), self.serverInfo)
            self.receiveMessage(client)

        elif message == "2":
            client.sendto('PORT'.encode(), self.serverInfo)
            self.receiveMessage(client)

        elif message == "3":
            current = 'TIMEDELAY' + str(datetime.utcnow())
            client.sendto(str(current).encode(), self.serverInfo)

            modifiedMessage, serverAddress = client.recvfrom(2048)
            splitMessage = modifiedMessage.decode().split(' ')

            print('Delay SENDING: ' + splitMessage[0])
            convertedServerTime = datetime.strptime(splitMessage[1]+' '+splitMessage[2],"%Y-%m-%d %H:%M:%S.%f")
            totalDelay = str(datetime.utcnow() - convertedServerTime)
            print('Delay RECEIVING: ' + totalDelay)

        elif message == '4':
            client.close()
            print("Exiting the client.")
            exit()

        else:
            client.sendto(message.encode(), self.serverInfo)
            self.receiveMessage(client)
        # else:
        #     print('Invalid selection.')