#Server program correponding to chat_client.py
import socket
import sys
import threading

class server:
    def __init__(self, host, port):
        self.s = socket.socket()
        self.connections = []
        try:
            self.s.bind((host, port))
            print("Server is online")
            self.s.listen(5)
        except Exception as e:
            print(str(e))
            sys.exit()
        
    def client_thread(self, client):
        buf_size = 2048
        while True:
            try:
                choice1 = client.recv(buf_size)
                choice = int(choice1.decode('utf-8'))
                if choice == 1:
                    to = int(client.recv(buf_size).decode('utf-8')) - 1
                    msg = client.recv(buf_size).decode('utf-8')
                    c = self.connections[to]
                    for x in self.connections:
                        if client in x:
                            frm = x[2]
                    c[0].sendall(("["+frm+"]: "+msg).encode())
                elif choice == 2:
                    i = 1
                    for c in self.connections:
                        x = str(i) + "." + str(c[2])
                        client.send(x.encode())
                        i += 1
                else:
                    client.close()
                    if client in self.connections:
                        self.connections.remove(client)
                    break
            except Exception:
                client.close()
                if client in self.connections:
                    self.connections.remove(client)
                break
        if client in self.connections:
            self.connections.remove(client)
        client.close()

    def Main(self):
        while True:
            try:
                client, addr = self.s.accept()
                name = client.recv(1024).decode('utf-8')
                self.connections.append([client, addr, name])
                print("Connected with ", name)
                threading._start_new_thread(self.client_thread, (client, ))
            except Exception as e:
                print(str(e))

host = ''
port = int(sys.argv[1])

s = server(host, port)
s.Main()
