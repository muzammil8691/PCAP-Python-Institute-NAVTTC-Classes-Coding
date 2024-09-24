
lst = [2,6,5,12,5,7,13,1]

swapped = True
while swapped:
    swapped = False
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            swapped = True
            lst[i], lst[i+1] = lst[i+1], lst[i]
print("Ascending order of list is: ",lst)



lst.reverse()
print("Descending order of list is: ",lst)


#-----------------------------------------------------------------------#
#----------------------Taking from user---------------------------------#
#-----------------------------------------------------------------------#


lst = []
swapped = True

num = int(input("How many numbers you want to sort? :"))

for i in range(num):
    var = int(input("Enter any number:" ))
    lst.append(var)

print(lst)

while swapped:
    swapped = False
    for i in range(len(lst)- 1):
        if lst[i]> lst[i+1]:
            swapped = True
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)




#-------------------#

