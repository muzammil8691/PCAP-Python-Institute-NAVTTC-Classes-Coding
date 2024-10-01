#----------------------------------------------------------------------------------#

def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
#This means that a function receives the argument's value, not the argument itself

#----------------------------------------------------------------------------------#
# Example 1
#only my wishes will be printed and not the "Happy birthday"

def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes

#----------------------------------------------------------------------------------#
#returning at start of function

def hi():
    return
    print("Hi")
print(hi())

#----------------------------------------------------------------------------------#
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(6.4))
print(is_int("10"))



#----------------------------------------------------------------------------------#

def even_lst(ran):
    lst= []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_lst(11))


#----------------------------------------------------------------------------------#



