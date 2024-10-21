#2.5.1.8 LAB: Anagrams


str1 = input("Enter first String: ")
str2 = input("Enter second String: ")

str1.replace(' ', '') #Removing space if any to not consider them
str2.replace(' ', '') #//

str1 = list(str1.lower()) #Converting string to list and lowering the CASE
str2 = list(str2.lower()) #//

def anagram(str1, str2):


    anagram = False
    for i in str1:
        if i in str2:
            anagram = True
        else:
            anagram = False
            return anagram
        return anagram
    

#Calling the function    
flag = anagram(str1, str2)
if flag == True:
    print("Anagram")
else:
    print("Not Anagram")
    