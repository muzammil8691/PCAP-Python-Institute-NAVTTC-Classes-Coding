#2.5.1.6 LAB: Improving the Caesar cipher


#Encryption
user_message = input("Enter a message to encrypt: ")
shift_value = int(input("Enter a shift value between 1-25 for encoding: "))

cipher = ''

for char in user_message:

    if char == ' ':
        cipher += char
    elif char.isdigit():
        cipher += char
    elif char.isupper():
        cipher += chr((ord(char) + shift_value - 65) % 26 + 65)
    else:
            cipher += chr((ord(char) + shift_value - 97) % 26 + 97)

print(cipher)


#Decryption

decode  = ''
for char in cipher:

    if char == ' ':
        decode += char
    elif char.isdigit():
        decode += char
    elif char.isupper():
        decode += chr((ord(char) - shift_value - 65) % 26 + 65)
    else:
        decode += chr((ord(char) - shift_value - 97) % 26 + 97)

print(decode)