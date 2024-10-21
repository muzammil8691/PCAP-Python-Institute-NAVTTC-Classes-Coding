# Caesar cipher.
#2.5.1.1

# every letter of the message is replaced by its nearest consequent 
# (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.


text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
