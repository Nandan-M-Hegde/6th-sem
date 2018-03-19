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
            msg = s.recv(4096).decode('utf-8')
            msg = msg.split('\t')
            if 'LS' in msg[0]:
                print(msg[1])
            else:
                fp = open(msg[0], "w")
                fp.write(msg[1])
                fp.close()
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
        fn = input("Filename: ")
        s.send(fn.encode())
        fp = open(fn, "r")
        msg = fp.read()
        s.sendall(msg.encode())
        print(">> ")
    elif choice == 2:
        continue
    else:
        s.close()
        sys.exit(0)