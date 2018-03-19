import socket
import sys
import threading
import os

class server:
    def __init__(self, host, port):
        self.s = socket.socket()
        try:
            self.s.bind((host, port))
            print("Server is online")
            self.s.listen(5)
        except Exception as e:
            print(str(e))
            sys.exit()
        
    def client_thread(self, client):
        buf_size = 2048
        ls = os.listdir()
        ls = '\t'.join(ls)
        client.send(ls.encode())

        while True:
            try:
                choice = client.recv(buf_size).decode('utf-8')
                if choice == '1':
                    fn = client.recv(buf_size).decode('utf-8')
                    fp = open(fn, "w")
                    print("Receiving file ", fn)
                    msg = client.recv(buf_size).decode('utf-8')
                    while msg != 'EOF':
                        fp.write(msg)
                        msg = client.recv(buf_size).decode('utf-8')
                    fp.close()
                    print(fn, " received")
                elif choice == '2':
                    fn = client.recv(buf_size).decode('utf-8')
                    if fn == '-1':
                        continue
                    fp = open(fn, "r")
                    data = fp.read().split('\n')
                    for line in data:
                        client.send((line + '\n').encode())
                    client.send('EOF'.encode())
                elif choice == '3':
                    continue
                else:
                    client.close()
                    return
            except Exception:
                client.close()
                return
        client.close()

    def Exit_thread(self):
        e = input()
        if "exit" in e:
            os._exit(1)

    def Main(self):
        threading._start_new_thread(self.Exit_thread, ())
        while True:
            try:
                client, addr = self.s.accept()
                print("Connected with ", addr)
                threading._start_new_thread(self.client_thread, (client, ))
            except Exception as e:
                print(str(e))

host = ''
port = int(sys.argv[1])

s = server(host, port)
s.Main()