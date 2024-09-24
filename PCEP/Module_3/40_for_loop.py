for i in range(10):
    print("The value of i is currently", i)

    #From 0 to 9

##
for i in range(2,10):  #the first argument determines the initial (first) value of the control variable.
    print("The value of i is currently", i)

    #From 2 to 9

###
for i in range(2, 10, 3):  #The range() function may also accept three arguments,The third argument is an increment
    print("The value of i is currently", i)

    #2,5,8

#there will be no output here
for i in range(2, 1):
    print("The value of i is currently", i)

    #No Result

for i in range(5,1,-1):
  print("The value of i is currently", i)

  #5,4,3,2

for x in range(-5, -10):
  print("the value of x is currently", x)

    #No Result

#Using String in for loop 
name = input("Enter your Name: ")
for i in name:
   print(i)