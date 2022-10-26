import socket
import os


# Opens the file with the given filename
# and sends its data over the network through the provided socket.
def send_file(socket, filename):
    if os.path.isfile(filename):
            socket.send("The file exists, do you want it (Y/N): ".encode()) #(3)
            socketResponse = socket.recv(1024).decode() #Gets the clients (Y/N) response
            if socketResponse == "Y":
                #Read file in binary
                file = open(filename, "rb")
                packet = file.read(1024)

                #Keeps sending data to the client
                while(packet):
                    socket.send(packet)
                    packet = file.read(1024)

                file.close()
                print("File has been transferred")
            
    else:
        socket.send("The file does not exist, exitting socket ".encode())
             

# Creates the file with the given filename
# and stores into it data received from the provided socket.
def recv_file(socket, filename):
    #Get filename
    socket.send(filename.encode())

    #Get's the "The file exists, do you want it (Y/N): " message from server
    data = socket.recv(1024).decode()
    print(data)

    #If file does not exist, the socket closes
    if data == "The file does not exist, exitting socket ":
        socket.close()
        print("Connection closed")


    #Sends (Y/N) to server
    else:
        fileConfirmation = input()
        socket.send(fileConfirmation.encode())

        #If file already exists, the socket will close
        if (os.path.isfile("new_" + filename)):
            print("The file already exists and you cannot overwrite it, the client will close now")
            socket.close()
            print("Connection closed")

        #Write file in binary
        file = open("new_" + filename, "wb")

        #Keep receiving data from the server
        packet = socket.recv(1024)

        while(packet):
            file.write(packet)
            packet = socket.recv(1024)

        print("File has been received")
        file.close()
        socket.close()
        print("Connection closed")
    


# Generates and sends the directory listing from
# the server to the client via the provided socket.
# send_listing(socket):


# Receives the listing from the server via the
# provided socket and prints it on screen.
# recv_listing(socket):