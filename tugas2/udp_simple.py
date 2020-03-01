
import socket

TARGET_IP = "10.151.252.191"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('KARINA SORAYA PUSPITASARI_05111740000003'.encode()),(TARGET_IP,TARGET_PORT))