john = 3
mary = 5 
adam = 6

print("John,", "Mary,", "Adam") #We can also use seperator as sep= ", "
print(john,"\t", mary,"\t", adam)


total_apples = john + mary + adam
print(total_apples)
print("Total number of apples are:", total_apples)



'''Concatination rule'''
#print("Total number of apples are:" + total_apples)
#This will give  an error cuz concatenation cannot be used with a variable (as total_apples is a variable)
