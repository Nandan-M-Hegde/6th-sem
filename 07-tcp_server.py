import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = int(sys.argv[1])

try:
    s.bind((host, port))
    print("Server is online...")
except:
    print("Server cannot be established")
    sys.exit(0)

s.listen(10)

client, addr = s.accept()
print(addr, " connected with server")
client.send("Welcome to server".encode())

while True:
    try:        
        msg = client.recv(2048).decode('utf-8')
        print(msg)
        if msg == 'REQUEST':
            print("Client request acknowldeged")
            client.send('OK'.encode())
            msg = client.recv(2048).decode('utf-8')
        elif msg == 'EXIT':
            break
        client.send(msg.upper().encode())
        print("Response sent")
    except:
        sys.exit(0)