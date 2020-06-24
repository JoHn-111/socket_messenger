import socket
import time
import threading
import os
from colorama import Fore, Style

br = False

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
    msgsend = '{' + username + ' connected}'
    msgsend = str.encode(msgsend)
    sock.sendto(msgsend, serv)
    print(Style.RESET_ALL)

    def send(run, sock, serv):
        while True:
            print(Fore.CYAN)
            message = input('~ ')
            if len(message) != 0:
                message = ('| ' + username + ' | => ' + message) 
                message = str.encode(message)
                sock.sendto(message, serv)
                time.sleep(0.1)
            print(Style.RESET_ALL)
            if br == True:
                break

    sendT = threading.Thread(target = send, args = ("sendThread", sock, serv))
    sendT.start()

    while True:
        data = sock.recv(1024)
        data = data.decode()
        connect_split = data.split()
        if connect_split[-1] == 'connected}':
            print(Fore.GREEN + printdata)
            connect_split.clear()
        else:    
            print(Fore.MAGENTA + ('\n' + data))
            print(Style.RESET_ALL)
        if br == True:
            break
    sendT.join()

except:
    br = True
    print(Fore.RED + ("connection loss..."))
