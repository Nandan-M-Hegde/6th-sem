#mc_server : Multiple client server
#Server program to accept messages from multiple clients and display them

import socket
import sys
import threading

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
        while True:
            try:
                msg = client.recv(buf_size).decode('utf-8')
                if not msg:
                    client.close()
                else:
                    print(msg)
            except Exception:
                client.close()
                break
        client.close()

    def Main(self):
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