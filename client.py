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
    HOST = input(Fore.YELLOW + Style.BRIGHT + ('Enter server address(ip): '))
    PORT = int(input(Fore.YELLOW + Style.BRIGHT + ('Enter server PORT: ')))
    username = input(Fore.YELLOW + Style.BRIGHT + ('Enter your name: '))
    clear()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    serv = (HOST, PORT)
    print(Style.RESET_ALL)
    print(Fore.GREEN + ('~~client connected~~').upper())
    print(Style.RESET_ALL)

    def send(run, sock, serv):
        while True:
            message = input('> ')
            if len(message) != 0:
                message = ('| ' + username + ' | => ' + message) 
                message = str.encode(message)
                sock.sendto(message, serv)
                time.sleep(0.1)

    sendT = threading.Thread(target = send, args = ("sendThread", sock, serv))
    sendT.start()

    while True:
        data = sock.recv(1024)
        data = data.decode()
        print(data)


    sendT.join()


except:
    sock.close()
    print(Fore.RED + ("connection loss..."))
