print("--------------------------Sorted() Method--------------------------")
# Demonstrating the sorted() function:
#The original list remains untouched.
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

print("--------------------------Sort() Method--------------------------")
# Demonstrating the sort() method:
#The second method affects the list itself - no new list is created.
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

print("--------------------------Sorting and Split--------------------------")

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)       #Where is the first element because W is capital 
print(s3[1])    #gives "are" 