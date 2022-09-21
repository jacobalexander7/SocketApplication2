This application implements a basic protocol for sending messages over TCP/UDP. 
The server can return: Client IP, Client Port, or a latency calculation.

Python 3.9.7 | Dependencies: socket, argparse, datetime, time

Command Line Instructions: 
1. Start the server application. 
Ex: python3 server.py -t TCP -p 8000
2. Start the client and supply connection information. Ex: python3 client.py -t TCP -i 127.0.0.1 -p 8000
3. Send a message from the client menu.

Defaults: 
IP = 127.0.0.1
Type = TCP
Port = 8000

New Update 9/21/22
---
Refactored classes for readability. 
Added response codes, invalid request handling, and server request logging. 


Design Explanation
---
Based on command line flags or defaults, the client/server creates TCP/UDP objects. These objects act as controllers, and a while loop is started from the main program. This while loop handles the connection and sending/receiving messages. 


Protocol Explanation
---
Client messages are prepended with a word indicating the command. The server looks up a response for the word and returns the relevant information. 

1. IP = 'IP' returns IP address of client
2. PORT = 'PORT' returns port of client
3. TIMEDELAY = 'TIMEDELAY<datetime>' returns the perceived latency of the message from client -> server 

Bugs
---
When closing a TCP client, the server will also close. I will refactor this to send a message before closing, so the server can reopen a listener.

Also when closing a TCP client, the server writes a log with blank METHOD. I read that the client is sending a FIN message before closing, so I need to handle that in the future. 