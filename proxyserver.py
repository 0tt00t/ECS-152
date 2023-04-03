from socket import *
import os

cache = {} # dictionary to store cached responses

serverPort = 8888
serverip = '0.0.0.0'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverip, serverPort))
serverSocket.listen(1)

print("The proxy server is ready to receive...")

while True:
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print("Received From Client: ", message)

        filename = message.decode().split()[1][1:]
        filetype = filename.split('.')[-1]

        if filename in cache:
            # if the response is in the cache, send it back to the client
            print("Cached response found!")
            connectionSocket.send(cache[filename])
        else:
            # otherwise, forward the request to the web server
            print("Forwarding request to web server...")
            webServerName = 'localhost'
            webServerPort = 80
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((webServerName,webServerPort))
            clientSocket.send(message)

            # receive the response from the web server
            response = b""
            while True:
                data = clientSocket.recv(1024)
                if not data:
                    break
                response += data

            # add the response to the cache and send it back to the client
            cache[filename] = response
            connectionSocket.send(response)

            # close the connection to the web server
            clientSocket.close()

        connectionSocket.close()

    except IOError:
        print("File not found!")
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n","UTF-8"))
        connectionSocket.close()

serverSocket.close()
