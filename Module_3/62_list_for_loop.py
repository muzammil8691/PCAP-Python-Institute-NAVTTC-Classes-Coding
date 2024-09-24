#For loop in list

for i in [1,2,3,4,5,6]:
    print(i)


#for loop in string

for i in "M.Muzammil":
    print(i)

#Playing with list in for loop

lst = [1,2,3,4,5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)




#Playing with list in for loop

mylist = []
for i in range(5):
    mylist.append(i + 1)
print(mylist)


#another

mylist = []
for i in range(5):
    mylist.insert(0, i + 1)
print(mylist)



#-----------Three Methods to play with list in for loop------------#

#First Method (Worst)
mylist = [2,3,4,5]
total = 0

for i in range(4):
    total += mylist[i]
print(total)


#Second Method (Not Recommennded)
mylist = [2,3,4,5]
total = 0

for i in range(len(mylist)):
    total += mylist[i]
print(total)



#Third Method (Recomended)
mylist = [2,3,4,5]
total = 0

for i in mylist:
    total += i
print(total)


