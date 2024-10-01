
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

#Positional
adding(2,3,4)

#Keyword
adding(c= 4, a= 2, b= 3)

#mixed 
#(Condition = use positional first and then keyword the opposite of this will give error)
adding(2, b=3, c=4)

#-------------------------More-On-Parameterized--------------------------------#


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.

introduction("John")
introduction("John","Khan")
