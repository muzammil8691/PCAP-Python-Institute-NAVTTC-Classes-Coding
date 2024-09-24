numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

#'''Appends/inserts a number at the end of the list'''

numbers.append(4)

print(len(numbers))
print(numbers)

#'''Adding a number in list by insert method at desired index'''

numbers.insert(0, 222)
print(len(numbers))
print(numbers)


numbers.insert(3, 10)
print(len(numbers))
print(numbers)



#Creating and polulation a list
my_list = []  # Creating an empty list.

print(type(my_list))

for i in range(5):
    my_list.append(i + 1)

print(my_list)

##Making use of lists
#Let's assume that you want to calculate the sum of all the values stored in the my_list list.
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
