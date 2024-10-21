# Numbers Processor.

#The third program shows a simple method allowing you to input a
#line filled with numbers, and to process them easily.
#Note: the routine input() function, combined together with the
#int() or float() functions, is unsuitable for this purpose

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for i in strings:
        total += float(i)
    print("The total is:", total)
except:
    print(i, "is not a number.")