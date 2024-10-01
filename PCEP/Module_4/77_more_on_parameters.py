#taking input from user and passing arguments 


def address(house, street, city, postal_code):
    print("Your address is:","House #",house, street, city, postal_code)

h= input("House No.: ")
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(h, s, c, p_c)



#--------------------------------------------------------#

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()


#--------------------------------------------------------#

# def add_numbers(a, b=2, c):
    #c gives error because it is followed by a default argument
#     print(a + b + c)

# add_numbers(a=1, c=3)

