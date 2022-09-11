from socket import *
from datetime import * 

class UDPClient():

    def __init__(self, serverIP, serverPort):
        self.serverInfo = (serverIP,serverPort)
        print(self.serverInfo)
        self.startup()

    def startup(self):
        client = socket(AF_INET, SOCK_DGRAM)
        print("Client started.")
        self.showMenu()

        while True:
            message = input('\nEnter the number for a command: ')
            self.send(client, message)

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
            print(str(current))
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
            print('Invalid selection.')

    def showMenu(self):
            print("Enter a number.\n1. IP\n2. PORT\n3. TIMEDELAY\n4. QUIT.\n")