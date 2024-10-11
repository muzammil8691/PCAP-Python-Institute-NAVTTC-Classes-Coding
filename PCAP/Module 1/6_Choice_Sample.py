#Using choice method
print("#--------------------Random-Choice-Method-------------------------#")

from random import choice

my_list = ['Apple', 'Banana', 'Grapes', 'Mango']

print(choice(my_list))

#-----------------------------------------------#

x = 'welcome'
print(choice(x))

print("#--------------------Random-Choices-Method-------------------------#")
#Can choose a list from which you want to show random
#But it also has repitition

from random import choices

my_list = ['Apple', 'Banana', 'Grapes', 'Mango']

print(choices(my_list, k=2))



print("#--------------------Random-Sample-Method-------------------------#")
#Gives random without repitition

from random import sample

my_list = ['Apple', 'Banana', 'Grapes', 'Mango']

print(sample(my_list, 3))