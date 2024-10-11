#NameSpace
#1. Built-in NameSpace
#2. Global NameSpace
#3. Local NameSpace
#4. Enclosing NameSpace

print("-----------------------Built-in NameSpace-----------------------")

print(len("Muzammil"))  #Here len is a namspace and also print is a namespace

#----------------------------------------------------------------------------#
print("-----------------------Global NameSpace-----------------------")

x = 5
print(x)

def num():
    global z
    z = 5
    print(z)
num()

#Here x and z are global namspaces

#----------------------------------------------------------------------------#


print("-----------------------Local NameSpace-----------------------")

a = 2 

def nmbr():
    a = 5
    print(a)

nmbr()
print(a)

#Here a = 2 is global and a = 5 is local and it cannot be used outside the function

#----------------------------------------------------------------------------#


print("-----------------------Enclosing NameSpace-----------------------")


def outer():
    b = 2

    def inner():
        print(b)

    inner()


outer()

#Here we are using b in nested function which is inside the outer() function. It is called enclosing namespace


