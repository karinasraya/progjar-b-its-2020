import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
port = 31000
server_address = ('localhost', port)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send data
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(100)
        amount_received += len(data)
        print(data)
        print(f"{data}")
finally:
    print("closing")
    sock.close()