import socket
import sys
import threading
import os

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
        
    def client_thread(self, client, name):
        buf_size = 2048
        while True:
            try:
                choice1 = client.recv(buf_size)
                choice = int(choice1.decode('utf-8'))
                if choice == 1:
                    to = int(client.recv(buf_size).decode('utf-8')) - 1
                    fn = client.recv(buf_size).decode('utf-8')
                    data = client.recv(buf_size).decode('utf-8')
                    c = self.connections[to]
                    msg = fn + '\t' + data
                    c[0].send(msg.encode())
                elif choice == 2:
                    i = 1
                    x = 'LS\t'
                    for c in self.connections:
                        if c[2] == name:
                            x += str(i) + "." + "You\n"
                        else:
                            x += str(i) + "." + str(c[2])
                            x += '\n'
                        i += 1
                    client.send(x.encode())                    
                else:
                    client.close()
                    for i in range(len(self.connections)):
                        if client in self.connections[i]:
                            self.connections.pop(i)
                    break
            except Exception:
                client.close()
                for i in range(len(self.connections)):
                        if client in self.connections[i]:
                            self.connections.pop(i)
                break
        client.close()

    def exit_thread(self):
        if input() == 'exit':
            os._exit(1)

    def Main(self):

        while True:
            try:
                client, addr = self.s.accept()
                name = client.recv(1024).decode('utf-8')
                self.connections.append([client, addr, name])
                print("Connected with ", name)
                threading._start_new_thread(self.client_thread, (client, name))
            except Exception as e:
                print(str(e))

host = ''
port = int(sys.argv[1])

s = server(host, port)
s.Main()