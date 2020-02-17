import sys
import socket
SIZE = 100
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
port = 31002
server_address = ('localhost', port)
print("starting up")
print(f"connecting from {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Accept Request
    request = connection.recv(SIZE)
    client_request = open(request.decode(),"rb")
    print("Request Accepted")
    # Receive the data in small chunks and retransmit it
    while True:
        received = client_request.read(SIZE)
        if not received :
            break
        connection.sendall(received)
        print("Send Data")
    # Clean up the connection
    connection.close()