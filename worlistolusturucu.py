import subprocess

print ("""
K   K  RRRR   EEEE   OOO   K   K  SSS
K  K   R   R  E     O   O  K  K   S
K K    RRRR   EEE   O   O  K K     SSS
K  K   R  R   E     O   O  K  K       S
K   K  R   R  EEEE   OOO   K   K  SSS 
-EXPLOİLT HACK TEAM
--discord:https://discord.gg/YT8KQC9Rm
""")


def secenek1():
    print("You chose option 1.")
    subprocess.run(["python", "dos.py"])

def secenek2():
    print("You chose option 2.")
    subprocess.run(["python", "porttarama.py"])

def secenek3():
    print("You chose option 3.")
    subprocess.run(["python", "data.py"])

def secenek4():
    print("You chose option 4.")
    subprocess.run(["python", "virüs.py"])

def secenek5():
    print("You chose option 5.")
    subprocess.run(["python", "Wordlist.py"])

def ana_menu():
    while True:
        print("Main menu:")
        print("DDOS TOOL 1")
        print("PORT SCAN 2")
        print("DATA&METHOD 3")
        print("Virüs total 4")
        print("Wordlist generator 5")
        print("Exit: Ctrl + c")
        
        secim = input("Select an option (1/2/3/4/5)>>> ")
        
        if secim == "1":
            secenek1()
        elif secim == "2":
            secenek2()
        elif secim == "3":
            secenek3()
        elif secim == "4":
            secenek4()
        elif secim == "5":
            secenek5()
        
            
            print("Successful!")

if __name__ == "__main__":
    ana_menu()

