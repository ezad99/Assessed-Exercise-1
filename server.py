from genericpath import isfile
import socket
import sys
import os
from server_client_functions import send_file

server_address = ("localhost",int(sys.argv[1]))

#Allows us to open device to other connections, AF = AddressFamily(Type of IP address accepted for connection)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created succesfully")

try:
    #Binds the socket to the address
    server_socket.bind(server_address)

    print(str(server_address) + "server up and running")

    #Configures how many clients the server can listen for simultaneously
    server_socket.listen(5)

    print("The server socket is listening")

except Exception as e:
	# Print the exception message
	print(e)

	# Exit with a non-zero value, to indicate an error condition
	exit(1)

while True:
    #Accepts a connection, returns (conn, address) where conn is a new socket object usable to send and receive data
    client_socket, client_address = server_socket.accept()

    client_socket_str = str(client_address)

    print("Client " + client_socket_str + "has successfully connected")

    #Get data from the client (Prints the "The client says hi" message)(1)
    connectionConfirmation = client_socket.recv(1024).decode()
    print(connectionConfirmation)

    #Receives the type of client request (get,put,list) and sends it back for confirmation
    client_request = client_socket.recv(1024).decode()
    client_socket.send(client_request.encode())
    

    if client_request == "get":
        #Get filename from client
        filename = client_socket.recv(1024).decode()
        
        #Determine if file is in directory

        send_file(client_socket,filename)
        # if os.path.isfile(filename):
        #     client_socket.send("The file exists, do you want it (Y/N): ".encode()) #(3)
        #     clientResponse = client_socket.recv(1024).decode() #Gets the clients (Y/N) response
        #     if clientResponse == "Y":
        #         #Read file in binary
        #         file = open(filename, "rb")
        #         packet = file.read(1024)

        #         #Keeps sending data to the client
        #         while(packet):
        #             client_socket.send(packet)
        #             packet = file.read(1024)

        #         file.close()
        #         print("File has been transferred")
            
        # else:
        #     client_socket.send("The file does not exist, exitting socket ".encode())

        client_socket.close()
        break

    # elif client_request == "put":

server_socket.close()




