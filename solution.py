# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind((webServer(), port))
    # Fill in start
    serverSocket.listen()
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() # Fill in start
        print(f"Connection from {addr} has been established.")
        #Fill in end
        try:

            try:
                message = connectionSocket.recv(1024) # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = connectionSocket.sendto(message.encode(),(webServer,port))  # Fill in start  #Fill in end

                # Send one HTTP header line into socket.
                # Fill in start
                serverSocket.send(outputdata)
                # Fill in end

                # Send the content of the requested file to the client
                connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n")
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                serverSocket.send("404 Not Found")
                # Fill in end

                # Close client socket
                # Fill in start
                connectionSocket.close()
                # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
