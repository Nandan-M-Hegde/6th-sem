import socket
import sys

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])

try:
    s.connect((host, port))
    msg = s.recv(2048).decode('utf-8')
    print(msg)
except:
    print("Could not connect to server")
    sys.exit(0)

while True:
    print("1.Send \n2.Exit")
    choice = input()
    if choice == '1':
        s.send('REQUEST'.encode())
        print("Request sent")
        msg = s.recv(2048).decode('utf-8')
        if msg == 'OK':
            print("Acknowledgement received \nServer available")
            msg = input("<< ")
            s.send(msg.encode())
            msg = s.recv(2048).decode('utf-8')
            print(">> ", msg)
        else:
            print("Server unavailable")
            continue            
    elif choice == '2':
        s.send('EXIT'.encode())
        s.close()
        sys.exit()