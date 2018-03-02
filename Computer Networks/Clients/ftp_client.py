import os
import sys
from ftplib import FTP

ftp = FTP('')
ftp.connect('', int(sys.argv[1]))
ftp.login(user = 'username', passwd = 'password')
ftp.cwd('.')
ftp.retrlines('LIST')

def upload_file():
    filename = input("Enter filename to upload: ")
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))

def download_file():
    filename = input("Enter filename to download: ")
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

while True:
    print("Menu")
    print("1.Upload \n2.Download \n3.Exit")
    choice = int(input())

    if choice == 1:
        upload_file()
    elif choice == 2:
        download_file()
    else:
        ftp.quit()
        break
