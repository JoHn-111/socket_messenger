import socket
import time
import threading
import os
from colorama import Fore, Style
import sys

HOST = '0'
PORT = 44347
def clear ():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')

clear()

tmp = os.popen("ip route show").read()
print(os.name)
print(tmp)
tmp = tmp.split()
print(tmp)
print(tmp[-3])


print(Fore.GREEN + "\n~~SERVER IS RUNNING~~")
print(Style.RESET_ALL)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    print(Fore.CYAN) 
    number_of_users = int(input('Number of participants: '))
    sock.listen(number_of_users)

    users = []
    
except:
    sock.close()

run_serv = True

def get_message_send(run, conn, addr): #run нужен без него не робит)
    try:
        run_serv = True
        while run_serv:
            data = conn.recv(1024)
            if not data:
                break
            if data != '':
                printdata = data.decode()               
                print(str(addr[1]) + " -> " + printdata)      
            for user in users:
                if user != conn:
                    user.send(data)
    except:
        sock.close()
try:
    while run_serv:
        conn, addr = sock.accept()
        gsmT = threading.Thread(target = get_message_send, args = ("get_message_sendThread",conn, addr))
        gsmT.start()    
        if addr not in users:
            users.append(conn)
except:
    sock.close()
    print(Style.RESET_ALL)
    print(Fore.RED + "\n~~SERVER IS STOPPED~~")

