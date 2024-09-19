#using \f \r and \ in print function
#\n and \fis for next line
#\t is for a Tab space
#\r removes all the string on the left side 
#Use only \ to use multiple line in source code but result will be displayed in one line in console.

print("The itsy bitsy spider \f climbed up the waterspout.")
print()
print("Down came the rain and \r washed the spider out.")
print()
print("Hello", "Python", "I Love Python")
print()


print("hello"\
      " my name"\
      " is"\
      " Muzammil")
print()




#using Seperator for spacing sep=""

print("Hello Guys", "this is a python class", sep=" ")
print()


str = "Python"
ver= 3
print(str, ver, sep="")
print()


#Using End for making it a single line end=
#if we use \n inside the end="\n" it will go to another line
print("The itsy bitsy spider climbed up the waterspout.", end= "")

print("Down came the rain and washed the spider out.")





#using \ in print. one \ gives error and \\ prints one of them
print("The itsy bitsy spider climbed up the waterspout.")
print("\\")
print("Down came the rain and washed the spider out.")



#Giving spaces after coma, or not has no effect in result
print("The itsy bitsy" , "spider climbed up the waterspout.")
print("The itsy bitsy","spider climbed up the waterspout.")



#if you want to print double quotes use single quotes in print function and double on only on the intended one
print('My name is "Muzammil" ')
print()
print("My name is 'Muzammil' ")
print()



#second method   (The \ actually ignores the next word and print it as it is. (we read it as escape))
print('My name is \"Muzammil\" ')



sn= "deadly"
print("Python is a", "Snake", sep = sn)