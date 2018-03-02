#This is client program for chat_server.py
import socket
import sys
import threading

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
s.connect((host, port))
name = input("Enter name: ")
s.send(name.encode())

def receive(s):
    while True:
        try:
            msg = s.recv(2048).decode('utf-8')
            if not msg:
                sys.exit(0)
            print(msg)
        except:
            sys.exit(0)
    
print("Menu")
print("1.Send \n2.Get client list \n3.Exit")

threading._start_new_thread(receive, (s, ))

while True:
    choice = int(input())
    s.send(str(choice).encode())
    if choice == 1:
        to = input("To: ")
        s.send(to.encode())
        msg = input()
        s.sendall(msg.encode())
    elif choice == 2:
        continue
    else:
        s.close()
        sys.exit(0)
