
#Literals
#Not only the integers are literals but all of them


print(type(2))

print(type(2.1))

print(type("2"))

print(type({1,2,3}))

print(type([1,2,3]))

print(type((1,2,3)))

print(type(True))


#Integers in Python

print(11,111,111) #Not considered as integer
#print(11 111 111) #Not considered as integer
print(11111111)   #Acceptable as integer
print(11_111_111) #to make a long integer readable use underscore in-betweeen


#Octal numbers (Octal numbers are prefixed by 0o) (Octals are between 0-7)
print(0o123)


#Hexadecimal numbers (Prefixed by 0x) (Hexa are between 0-9 & a-f)

print(0x4b12)

# The answer in console will be converted into a decimal number by the interpreter



#Floats


print(4.0)
print(.4)
print(4.)
print(0.4)

#All are same

print(type(3000000000000))
print(3e12) #e represents exponent which is a float
print(type(3e12))
print(3*10**12) #double * means power(in this case 10 is to power 12)




#Question 6.62607 x 10 power -34 can be written in python as?
print(6.62607e-34)


#Using Backslash
print("I'm Monty Python.")
print('I\'m Monty Python.')




