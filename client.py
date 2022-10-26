import socket
import sys
import os
from server_client_functions import recv_file

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (sys.argv[1], int(sys.argv[2]))

client_request =  sys.argv[3] #Gets the clients request (put,get,list)

filename = sys.argv[4]

server_address_string = str(server_address)

#Connected sockets
try:
	print("Connecting to " + server_address_string + "... ")

	client_socket.connect(server_address)
	
	print("Connected")
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)


#Connect to server
client_socket.send("The client says hi ".encode())

#Send the client request (get,put,list) to server and receive it back to confirm it
client_socket.send(client_request.encode())
client_request = client_socket.recv(1024).decode()

if client_request == "get":
    recv_file(client_socket,filename)
    # #Get filename
    # client_socket.send(filename.encode())

    # #Get's the "The file exists, do you want it (Y/N): " message from server
    # data = client_socket.recv(1024).decode()
    # print(data)

    # #If file does not exist, the socket closes
    # if data == "The file does not exist, exitting socket ":
    #     client_socket.close()
    #     print("Connection closed")


    # #Sends (Y/N) to server
    # else:
    #     fileConfirmation = input()
    #     client_socket.send(fileConfirmation.encode())

    #     #If file already exists, the socket will close
    #     if (os.path.isfile("new_" + filename)):
    #         print("The file already exists and you cannot overwrite it, the client will close now")
    #         client_socket.close()
    #         print("Connection closed")

    #     #Write file in binary
    #     file = open("new_" + filename, "wb")

    #     #Keep receiving data from the server
    #     packet = client_socket.recv(1024)

    #     while(packet):
    #         file.write(packet)
    #         packet = client_socket.recv(1024)

    #     print("File has been received")
    #     file.close()
    #     client_socket.close()
    #     print("Connection closed")





