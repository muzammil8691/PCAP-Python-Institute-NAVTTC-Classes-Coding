#Reversing the list elements

my_list = [10, 1, 8, 3, 5,6,7]
print(my_list)

my_list[0], my_list[6] = my_list[6], my_list[0]
my_list[1], my_list[4] = my_list[4], my_list[1]

print(my_list)


# now with a built-in function

my_list.reverse()

print(my_list)


#Generic Code for reversing the list items

my_list = [10, 1, 8, 3, 5,1,2,9]
length = len(my_list)

for i in range(length // 2): # for i in range(3): 0,1,2
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


#Trying new method by myself (Still Incomplete)

my_list = [10, 1, 8, 3, 5,1,2,9]
length = len(my_list)

for i in range(len(my_list)): # for i in range(3): 0,1,2
    my_list[i], my_list[- 1 - i] = my_list[- 1 - i], my_list[i]
    
print(my_list)

