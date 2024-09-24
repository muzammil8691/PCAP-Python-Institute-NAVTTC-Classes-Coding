#Logic without hiding the entered word

while True:
    secret_word = input("Enter a word: ")
    if secret_word == "chupacabra":
        break
print("You've successfully left the loop.")

#Using the getpass module/package to hide the input

import getpass
while True:
    secret_word = getpass.getpass("Enter a word: ")
    if secret_word == "chupacabra":
        break
print("You've successfully left the loop.")