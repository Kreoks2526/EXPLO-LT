import random
import string

def generate_custom_wordlist(name, size):
    # Create the custom wordlist
    custom_wordlist = []
    for _ in range(size):
        # Generate a variation of the name with random characters
        random_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(name)))
        custom_wordlist.append(random_name)

    return custom_wordlist

def main():
    print("Merhaba! Özel kelime listesi oluşturmak için aşağıdaki bilgileri girin:")
    name = input("Lütfen bir isim girin (örneğin, Ahmet): ")
    size = int(input(f"{name}, kaç farklı kelime oluşturmak istersiniz? "))

    custom_wordlist = generate_custom_wordlist(name, size)

    print(f"{name}, işlem tamamlandı! Özel kelime listesi aşağıdaki gibidir:")
    for word in custom_wordlist:
        print(word)

if __name__ == "__main__":
    main()
