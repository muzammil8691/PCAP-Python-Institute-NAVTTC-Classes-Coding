user_input = input("Please Enter a Word: ")

word_without_vowels = ""

for letter in user_input:
    if letter == "a" or letter == "A":
        continue
    elif letter == "e" or letter == "E":
        continue
    elif letter == "i" or letter ==  "I":
        continue
    elif letter == "o" or letter == "O":
        continue
    elif letter == "u" or letter == "U":
        continue
    else:
        print(letter, end="")
        word_without_vowels = word_without_vowels + letter
print()        
print(word_without_vowels)

print()
#Alternate Method


user_input = input("Please Enter a Word: ")
result = ""

for letter in user_input:
    if letter.lower() in "aeiou":
        continue
    else:
        result = result + letter

print(result)

