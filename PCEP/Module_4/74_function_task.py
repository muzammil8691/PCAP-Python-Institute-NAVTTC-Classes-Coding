#----------------------------Code-01---------------------------------------#
#Code Without function(Bad Code)
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())


#----------------------------Code-02---------------------------------------#
#Code using Function
def intro_fun():
    #Getting input from user #docstring
    a = int(input("Enter a value: "))
    print(a)

intro_fun()    
intro_fun()    


#----------------------------Code-03---------------------------------------#
#Using Return in Function
def taking_value():
    #This function will take value from user and return it #docstring
    x = int(input("Enter a value: "))
    return(x)

a = taking_value()
print("Value of a is ", a)

b = taking_value()
print("Value of b is ", b)

c = taking_value()
print("Value of c is ", c)

