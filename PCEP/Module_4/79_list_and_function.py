#Passing list to a function as a argument and playing with it

def list_sum(lst):
    s = 0
    for i in lst:
        s += i

    return s

print("The function containing list returns: ",list_sum([2,3,5]))

#-----------------------------------------------------------------#
#May a function return result as a string


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
