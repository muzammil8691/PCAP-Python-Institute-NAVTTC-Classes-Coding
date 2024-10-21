#2.5.1.10 LAB: Find a word!

str1 = input("Enter the word you want to check for: ")
str2= input("Enter the String you want to find in: ")

def find_word(str1, str2):
    for i in str1:
        result = str2.find(i)
        if result == -1:
            return "No"
        else:
            continue
    return "Yes"        
    


print(find_word(str1, str2))
