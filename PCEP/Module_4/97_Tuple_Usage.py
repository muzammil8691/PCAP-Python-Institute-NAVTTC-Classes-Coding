#How to use tuples

my_tupple = (1,2,3,4,5)

print(my_tupple[0])
print(my_tupple[-1])
print(my_tupple[1:])
print(my_tupple[:-2])

for elem in my_tupple:
    print(elem)


#----------------------------------------------------------------#
#These things works with Tuple


my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)           #Concat
t2 = my_tuple * 3                       #Replication

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#----------------------------------------------------------------#


tup = (1,2,3)
tup = tup + (4,5,6) 
print(tup)

#----------------------------------------------------------------#





