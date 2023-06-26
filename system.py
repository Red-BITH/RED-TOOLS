import socket
import os
os.system("pip install socket")

os.system("clear")


def banner_saxlama(hedef_ip, port):
    try:
       
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(5)  

        
        soket.connect((hedef_ip, port))

       
        soket.send(b"GET / HTTP/1.1\r\n\r\n")

        
        banner = soket.recv(1024)
        
        print("\033[92m[+] Hədəf IP: \033[0m", hedef_ip)
        print("\033[92m[+] Port: \033[0m", port )
        print("\033[92m[+] Banner Bilgisi:\033[0m")
        print(banner.decode().strip())

        
        soket.close()

    except Exception as e:
        print("[-] Hata:", str(e))


# Banner yakalamak istediğiniz hedef IP adresini ve portunu belirtin
print("\033[92mİP DAXİL ET(SİTE İP Sİ DOĞRU OLMALIDIR! )! \033[0m")
print("\033[91m SITE PHP OLMAMALIDIR! \033[0m")
hedef_ip = (input(" İP DAXİL ET:"))

print("""\033[92mPort seçimi edirsiniz? yoxsa DEFAULT?
1--(BƏLİ)
2--(DEFAULT)\033[0m""")
t = input("DAXİL ET:")
if(t == "1"):
    port = input(int("DAXİL ET:"))
elif(t == "2"):
    port = 80
else:
    port = 80
banner_saxlama(hedef_ip, port)


