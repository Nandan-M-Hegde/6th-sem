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
                    fn = client.recv(buf_size).decode('utf-8')
                    data = client.recv(buf_size).decode('utf-8')
                    c = self.connections[to]
                    for x in self.connections:
                        if client in x:
                            frm = x[2]
                    c[0].sendall(fn.encode())
                    c[0].sendall(data.encode())
                elif choice == 2:
                    i = 1
                    x = ''
                    for c in self.connections:
                        x += str(i) + "." + str(c[2])
                        x += '\t'
                        i += 1
                    client.send('LS'.encode())
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