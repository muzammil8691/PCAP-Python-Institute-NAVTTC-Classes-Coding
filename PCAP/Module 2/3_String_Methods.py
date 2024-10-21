#It affects only the first letter of the string. 
#The remaining characters are converted to lowercase.

print("--------------------- Capitalize ---------------------")
my_string = "hello, World!. ihsan"

# Capitalize the string
capitalized_string = my_string.capitalize()

print(capitalized_string)  # Output: "Hello, world!"
print("Alpha".capitalize()) #Outputs: Alpha
print('ALPHA'.capitalize()) #Outputs: Alpha
print(' Alpha'.capitalize())#Outputs:  alpha

print("--------------------- Title ---------------------")
#Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()

print(x)

print("--------------------- Upper Case ---------------------")
#Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()

print(x)

print("--------------------- Lower Case ---------------------")
#Lower case the string:
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

print("--------------------- Swap Case ---------------------")
#Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()

print(x)

print("--------------------- Center ---------------------")
#Print the word "banana", taking up the space of 20 characters,
# with "banana" in the middle:
txt = "banana"
print(txt)

x = txt.center(20)
print(x)

print("--------------------- Count ---------------------")
#Return the number of times the value "apple" appears in the string
txt = "I love apples, apple are my favorite fruit"

x = txt.count("f")
y = txt.count("apples")

print(x)
print(y)
