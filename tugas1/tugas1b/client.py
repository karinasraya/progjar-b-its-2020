import sys
import socket
SIZE = 100
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
port = 31002
server_address = ('localhost', port)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send Request
    message = 'send.txt'
    print(f"sending {message} as request")
    sock.sendall(message.encode())
    # Look response
    respon_received = open("received.txt", "wb")
    if not respon_received:
        print("Request Rejected\n")
    respon_received.write(sock.recv(SIZE))
    print("Request Accepted\n")

finally:
    sock.close()