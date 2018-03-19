import socket
import sys
import os
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = ''
port = int(sys.argv[1])
s.bind((host, port))
print("Server is online...")

def Exit_thread():
    ip = input()
    if "exit" in ip:
        os._exit(1)

while True:
    threading._start_new_thread(Exit_thread, ())
    data, addr = s.recvfrom(2048)
    data = data.decode('utf-8')
    print("Received \"", data, "\" from ", addr)
    data = data.upper()
    s.sendto(data.encode(), addr)
    print("Sent \"", data ,"\" to ", addr)