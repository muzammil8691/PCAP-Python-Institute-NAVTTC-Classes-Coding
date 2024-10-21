# Convert character to ASCII value

print("---------Convert character to ASCII value---------")
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")



# Convert ASCII to Character value
print("---------Convert ASCII to Character value ---------")
ascii = 65

char_value = chr(ascii)
print(f"The Char value of '{ascii}' is {char_value}")


print("---------------A little Tricky Question---------------")
for ch in "abc":
    print(chr(ord(ch) + 1), end="")