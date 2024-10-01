#--------------------Code-01--Squares-----------------------#
#traditional method

squares = []

for i in range(10):
    squares.append(i**2)

print(squares)


#Now by list comphrension
# variable name = [ expression  for loop and condition(if any)]

squares = [i**2 for i in range(10)]
print(squares)


#--------------------Code-02--Odd-----------------------#
#traditional method


odd= []
squares = [1,2,3,4,5,6,7,8,9]

for x in squares:
    if x % 2 != 0:
        odd.append(x)

print(odd)


#Now by list comphrension 
# variable name = [ expression  for loop and condition(if any)]

squares = [1,2,3,4,5,6,7,8,9]

odd = [x for x in squares if x % 2 == 0]
print(odd)



#--------------------Code-03--Fruits-----------------------#
#traditional method


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)



#Now by list comphrension 
# variable name = [ expression  for loop and condition(if any)]

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits if 'a' in x ]
print(newlist)




#--------------------Code-04--Words-----------------------#
#traditional method


lst = ['hello', 'python', 'java', 'muzammil']

new_lst= []

for x in lst:
    if len(x)>5:
        new_lst.append(len(x))
        # print(f"length of {x} = {len(x)}") 
print(new_lst)       


#Now by list comphrension 

lst = ['hello', 'python', 'java', 'muzammil']

new_lst = [len(x) for x in lst if len(x)>5 ]
print(new_lst)




#--------------------Code-05--Common--Numbers-----------------------#
#traditional method

lst_1 = [1,2,3,4,5,6]
lst_2 = [3,6,9,4,2]

lst_new = []

for x in lst_1:
    if x in lst_2:
        lst_new.append(x)
print(lst_new)



#Now by list comphrension

lst_1 = [1,2,3,4,5,6]
lst_2 = [3,6,9,4,2]

lst_new = [ x for x in lst_1 if x in lst_2]
print(lst_new)