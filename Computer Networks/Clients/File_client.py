import socket
import sys
import threading

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
s.connect((host, port))

msg = s.recv(4096).decode('utf-8')
ls = msg.split('\t')

while True:    
    print("Menu")
    print("1.Put \n2.Get \n3.List \n4.Exit")
    choice = input()
    s.send(choice.encode())

    if choice == '1':
        fn = input("File name: ")
        s.send(fn.encode())
        fp = open(fn, "r")
        data = fp.read().split('\n')
        for msg in data:
            s.send((msg+'\n').encode())
        s.send('EOF'.encode())
        if fn not in ls:
            ls.append(fn)
        
    elif choice == '2':
        fn = input("File name: ")
        if fn not in ls:
            print("file does not exist")
            s.send('-1'.encode())
            continue
        s.send(fn.encode())
        msg = s.recv(2048).decode('utf-8')
        fp = open(fn, "w")
        while True:
            fp.write(msg)
            msg = s.recv(2048).decode('utf-8')
            if 'EOF' in msg:
                print("End of file")
                fp.close()
                break
    elif choice == '3':
        for fn in ls:
            print(fn)
    else:
        s.close()
        break
sys.exit(0)