from socket import *
serverPort = 8000


# SOCK_DGRAM = UDP
# SOCK_STREAM = TCP

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048) #Taking 2048 bytes
    print(message)
    modifiedMessage = message.decode().upper()  #Use the decode method to process as string
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) #Re-encode the string as bytes
