print("""
 1- Andoroid virüs     3- Coming soon  6-Coming soon   7-Coming soon   9-Coming soon
2- Andoroid virüs2     4- Coming soon  5-Coming soon    8-Coming soon  10-Coming soon
""")


secenekler = ["Andoroid virüs 1", "Andoroid virüs2 2", "Seçenek 3", "Seçenek 4", "Seçenek 5", "Seçenek 6", "Seçenek 7", "Seçenek 8", "Seçenek 9", "Seçenek 10"]

# Kullanıcının seçtiği sıradaki seçeneği belirle
secim = int(input("Please enter a sequence of options (1-10): "))

# Kullanıcının seçtiği sıradaki seçeneği kontrol et ve belirlenen cevabı yazdır
if 1 <= secim <= 10:
    cevaplar = ["https://unforgettable.dk/", "https://justpaste.it/redirect/6nvkc/https%3A%2F%2Fdosya.co%2F1chj8c5vhudd%2FBB_DDOS_ATTACK.apk.htmla", "", "", "", "Sandalye", "", "", "", ""]
    secilen_secenek = secenekler[secim - 1]
    cevap = cevaplar[secim - 1]
    if cevap:
        print(f"Seçiminiz ({secilen_secenek}): {cevap}")
    else:
        print(f"Seçiminiz ({secilen_secenek}) için bir cevap bulunamadı.")
else:
    print("Geçersiz seçim. Lütfen 1 ile 10 arasında bir sayı girin.")
