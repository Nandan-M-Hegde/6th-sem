import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
print("Enter message: ")

while True:
    msg = input()
    if "exit" in msg:
        break
    s.sendto(msg.encode(), (ip, port))
    msg = s.recv(2048).decode('utf-8')
    print(msg)