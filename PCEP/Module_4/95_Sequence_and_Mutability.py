#Mutable data can be freely updated at any time (List is Mutable)

#Immutable data can be freely updated at any time

#------------------------------------------------------------#
#immutable
my_tuple = (1, 10, 100, 1000)

my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
print(my_tuple)

#------------------------------------------------------------#
#mutable

my_list = [1, 10, 100, 1000]

my_list.append(10000)
del my_list[0]
my_list[1] = -10
print(my_list)