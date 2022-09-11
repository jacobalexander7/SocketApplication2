from socket import *
from datetime import * 

class TCPClient():

    def __init__(self, serverIP, serverPort):
        self.startup(serverIP, serverPort)

    def startup(self, serverIP, serverPort):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((serverIP, serverPort))
        print("Client started.")
        self.showMenu()

        while True:
            message = input('\nEnter number for command: ')
            self.send(client, message)

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
            print(str(current))
            client.send(str(current).encode())
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