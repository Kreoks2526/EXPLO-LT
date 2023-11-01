print("""
K   K  RRRR   EEEE   OOO   K   K  SSS
K  K   R   R  E     O   O  K  K   S
K K    RRRR   EEE   O   O  K K     SSS
K  K   R  R   E     O   O  K  K       S
K   K  R   R  EEEE   OOO   K   K  SSS 
-EXPLOİLT HACK TEAM
""")      


def ana_menu():
    while True:
        print("MAIN MENU:")
        print("1. DATA")
        print("2. METHOD")
        print("3. Çıkış")
        
        secenek = input("Bir seçenek girin (1/2/3): ")

        if secenek == "1":
            secim = sey_sec()
            if secim is not None:
                print(f"İnstagram data:https://dosya.co/j9sip9ze7rfr/LİL4TEEN_İNSTA_DATA.rar.html")
        elif secenek == "2":
            secim = diger_sey_sec()
            if secim is not None:
                print(f"twitter:https://ay.live/W4yC")
        elif secenek == "2":
            secim = diger_sey_sec()
            if secim is not None:
                print(f"Telegram:https://anonfiles.com/HbXec737o5/Telegram_csv_rar")
        elif secenek == "3":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

def sey_sec():
    secenekler = {
        "1": "İnstagram data",
        "2": "twitter data",
        "3": "Telegram data",
        "4": "Country data",
        "5": "More data"
    }
    
    print("Lütfen bir seçenek numarası girin (1-5):")
    for secenek, sey in secenekler.items():
        print(f"{secenek}. {sey}")
    
    secim = input("Seçiminizi girin: ")
    
    if secim in secenekler:
        return secenekler[secim]
    else:
        print("Geçersiz seçenek! Lütfen geçerli bir numara girin.")
        return sey_sec()

def diger_sey_sec():
    secenekler = {
        "1": "Coming soon",
        "2": "Coming soon",
        "3": "Coming soon",
        "4": "Coming soom",
        "5": "Coming soon"
    }
    
    print("Lütfen bir seçenek numarası girin (1-5):")
    for secenek, sey in secenekler.items():
        print(f"{secenek}. {sey}")
    
    secim = input("Seçiminizi girin: ")
    
    if secim in secenekler:
        return secenekler[secim]
    else:
        print("Geçersiz seçenek! Lütfen geçerli bir numara girin.")
        return diger_sey_sec()

if __name__ == "__main__":
    ana_menu()
