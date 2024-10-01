#inner Life of List

lst1 = [1,4]
lst2 = lst1

print(lst2)

lst1[0] = 2
print(lst2)
print(lst1)

#Both targeting the same memory location so they will give same answer
#To overcome this problem we use slice

lst_1 = [1,3,5]
lst_2 = lst_1[:]
print(lst_1, lst_2)

lst_3 = lst_1[0:2]
print(lst_3)

lst_4 = lst_1[:2]
print(lst_4)

lst_5 = lst_1[1:]
print(lst_5)
