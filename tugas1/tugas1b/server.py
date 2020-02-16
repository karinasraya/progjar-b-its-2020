import sys
import socket
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
    # Receive the data in small chunks and retransmit it
    fl = open("send.txt", 'rb')
    konten = fl.read(100)
    message = str(konten)
    print(f"sending {message}")
    connection.sendall(message.encode())
    # Clean up the connection
    connection.close()