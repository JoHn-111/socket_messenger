import socket
import time
import threading
import os
from colorama import Fore, Style

def clear ():
    global PORT, HOST 
    if os.name == 'nt':
        os.system ('cls')
        PORT = int(input(Fore.YELLOW + Style.BRIGHT + ('Enter PORT: ')))
        HOST = input('Enter your IPv4 Address(use command " ipconfig "): ')
        print(Fore.YELLOW + Style.BRIGHT + ('use this ip when starting the client-->>  ').upper() + str(HOST))
        print(Fore.YELLOW + Style.BRIGHT + ('use this PORT when starting the client-->>  ').upper() + str(PORT))
    else:
        os.system ('clear')
        PORT = int(input(Fore.YELLOW + Style.BRIGHT + ('Enter PORT: ')))
        HOST = '0'
        tmp = os.popen("ip route show").read()
        tmp = tmp.split()
        if len(tmp) > 16:
            print(Fore.YELLOW + Style.BRIGHT + ('use this ip when starting the client-->>  ').upper() + tmp[-3])
            print(Fore.YELLOW + Style.BRIGHT + ('use this PORT when starting the client-->>  ').upper() + str(PORT))  
        else:
            print(Fore.YELLOW + Style.BRIGHT + ('use this ip when starting the client-->>  ').upper() + tmp[-1])   
            print(Fore.YELLOW + Style.BRIGHT + ('use this PORT when starting the client-->>  ').upper() + str(PORT))   

clear()
try:
    number_of_users = int(input('Number of participants: '))
    print(Fore.GREEN + "\n~~SERVER IS RUNNING~~")
    print(Style.RESET_ALL)


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    print(Fore.CYAN) 
    
    sock.listen(number_of_users)
    users = []   
    run_serv = True
except:
    sock.close()

def get_message_send(run, conn, addr): #run нужен без него не робит)
    try:
        run_serv = True
        while run_serv:
            data = conn.recv(1024)
            if not data:
                break
            if data != '':
                printdata = data.decode() 
                connect = printdata
                connect_split = connect.split()
                print(connect_split)
                if connect_split[-1] == 'connected}':
                    print(Fore.GREEN + printdata)
                    connect_split.clear()
                    print(Fore.CYAN)
                else:            
                    print(printdata)
    
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
