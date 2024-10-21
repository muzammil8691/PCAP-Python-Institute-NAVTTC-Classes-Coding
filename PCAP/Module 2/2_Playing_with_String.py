#Multiline String
print("----------------#Multiline String---------------------")

print('''
    dsfsd
      sdfsdf
        sdfsdf
            sdfsdf
      ''')


#Length with Escape Character
print("----------------------Length with Escape Character--------------------------")

print(len("\n\n"))
#length would be 2. cuz backslash ecsapes the next character. It will not be counted.



#Playing with Concat-Replication
print("-----------------------Playing with Concat-Replication----------------------------")

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)


#Creating a List which contains all the string characters
print("----------------Creating a List which contains all the string characters------------------------")

my_str = ("Muhammad Muzammil")

lst = list(my_str)
print(lst)



#Printing the maximum value(based in ascii)
print("----------------Printing the maximum value(based in ascii)------------------")

new_str = "Aa"
print(max(new_str)) #cuz ascii of a is 97


#Printing the minimum value(based in ascii)
print("----------------Printing the minimum value(based in ascii)------------------")

new_str = "Aa"
print(min(new_str)) #cuz ascii of A is 65


#Index of string
print("----------------Index of string------------------")

name = "Muzammil"

index = name.index('i')
print(index)


print("----------------Index of Empty string (Multi-Line)------------------")
str_1 = '''
'''
print(len(str_1))  
#Gives the length 1 cuz enter is counted as \n. backslash is counted a escape character and n is counted

print("----------------Conveting String to List and printing with index------------------")

s = "yesteryears"
the_list= list(s)

print(the_list[0:6])
print(the_list[6:])


