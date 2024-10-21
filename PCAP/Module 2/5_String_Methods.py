print("--------------------- Replace ---------------------")
#Returns a string where a specified value is replaced with a specified value
#Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")

print(x)

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)

print("--------------------- Find ---------------------")
#Searches the string for a specified value and returns the last position 
#of where it was found.
#Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")

print(x)
# find between 5 and 10 only
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)

print(x)

print("--------------------- Split ---------------------")
#Splits the string at the specified separator, and returns a list
#Split a string into a list where each word is a list item
txt = "welcome to the jungle"
x = txt.split()

print(x)
print(x[0])
#Split the string, using comma, followed by a space, as a separator
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")

print(x)


print("--------------------- Join ---------------------")
#Join all items in a tuple into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)