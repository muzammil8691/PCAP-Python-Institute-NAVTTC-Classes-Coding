my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0
print(my_list)

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']



#---------------------------------------------------------------------------------------------#
#Deleting in list with defining range


lst = [1,2,3,4,5,6]
print(lst)

del lst[2:4]
print(lst)

del lst

#----------------------------------------------------------------------------------------------#
#Remove method in list

colors = ["Green", "Blue", "Yellow", "Green"]
print(colors)

colors.remove("Green")
print(colors)

#----------------------------------------------------------------------------------------------#
#Difference between del and clear
#del deletes the list existance and clear removes the elements only

colors = ["Green", "Blue", "Yellow", "Green"]

colors.clear()
print(colors)

del colors
# print(colors)


#----------------------------------------------------------#
#Using extend to add elements
print()


lst = [1,2,3]
lst.append(4)
print(lst)
print(len(lst))


lst.extend(['a','b','c'])
print(lst)
print(len(lst))


del lst[1:3]
print(lst)