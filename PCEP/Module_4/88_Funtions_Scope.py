#Scope of teh Function
#Variable defined in function cannot be accessed outside the function

def scope_test():
    x = 123


scope_test()
#print(x)

#----------------------------------------------------------#
#Variable defined outside can be accessed inside the function

def my_fun():
    print("Do I know the variable?", var)

var = 1 
my_fun()
print(var)


#----------------------------------------------------------#
#internal value of variable in function is not affecting the variable outside

def another_fun():
    var = 2 
    print("Do I know the variable?", var)

var = 1 
another_fun()
print(var)


#----------------------------------------------------------#
#using the keyword global inside the function

def another_fun():
    global var
    var = 2 
    print("Do I know the variable?", var)

var = 1 
another_fun()
print(var)

