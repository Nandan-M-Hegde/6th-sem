import socket
import sys

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])

try:
    s.connect((host, port))

    print("Type your message and press [ENTER] to send")
    print("Send \"Exit\" or \"exit\" to exit")
    msg = str(input())

    while True:
        if "exit" in msg or "Exit" in msg:
            s.close()
            break
        else:
            s.sendall(msg.encode())
            msg = input()

except Exception as e:
    print(str(e))
    s.close()
