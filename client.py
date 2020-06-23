import socket
import time
import threading
import os
from colorama import Fore, Style

def clear ():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')

clear()
try:
    HOST = input('enter server address: ')     #'192.168.1.66'
    clear()
    PORT = 44349
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    serv = (HOST, PORT)   #"109.252.72.210"

    print('client connected')


    def send(run, sock, serv):
        while True:
            message = input('>> ')
            if len(message) != 0:
                message = str.encode(message)
                sock.sendto(message, serv)
                print('message sended')
                time.sleep(0.2)

    sendT = threading.Thread(target = send, args = ("sendThread", sock, serv))
    sendT.start()

    while True:
        data = sock.recv(1024)
        data = data.decode()
        print("=> " + data)


    sendT.join()
    sock.close()

except:
    sock.close()
    print("connection loss...")
