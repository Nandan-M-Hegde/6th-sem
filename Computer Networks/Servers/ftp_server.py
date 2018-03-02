import os
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#Gets the current working directory
current_dir = os.getcwd()

#Instantiates dummy authorizer for managing users
authorizer = DummyAuthorizer()

#Defines a new user having full permissions
authorizer.add_user('username', 'password', current_dir, perm='elradfmw')

#Defines an anonymous user with only read permission
authorizer.add_anonymous(current_dir)

#Instantiates ftp handler class
handler = FTPHandler
handler.authorizer = authorizer

#Defines a banner which is a string returned whenever a client connects to server
handler.banner = "Welcome to server"

#Instantiates FTPserver class and listens on given ip and port
address = ('', int(sys.argv[1]))
server = FTPServer(address, handler)

#Sets a limit on connections
server.max_cons = 256
server.max_cons_per_ip = 5

#Starts the server
server.serve_forever()
