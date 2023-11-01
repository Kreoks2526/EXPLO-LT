import random
import string

print("""
#######################################
# CODE BY-KREOKS                      #
#-EXPLOİLT HACK TEAM                  #
#                                     #
#-WORDLIST GENERATOR                  #
#-discord:https://discord.gg/YT8KQC9Rm #
#######################################
      
""")

import random
import string

def generate_wordlist(name, size, length):
    # List of lowercase letters, uppercase letters and numbers
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Create the wordlist
    wordlist = []
    for _ in range(size):
        word = ''.join(random.choice(letters) for _ in range(length))
        wordlist.append(word)

    return wordlist, name

def main():
    print("Hello! Enter the following information to create a word list:")
    name = input("Please enter a name (for example, John): ")
    size = int(input(f"{name}, How many lines of a word list would you like to create? "))
    length = int(input(f"{name}, How many characters should each word be? "))

    wordlist, user_name = generate_wordlist(name, size, length)

    print(f"{user_name}, iprocess completed! The word list is as follows:")
    for word in wordlist:
        print(word)

if __name__ == "__main__":
    main()

print("Don't you like our program? No problem, join our discord address and join cuppvb. We can teach people how to create a worlist specifically! Our discord sevrer:https://discord.gg/YT8KQC9Rm")
