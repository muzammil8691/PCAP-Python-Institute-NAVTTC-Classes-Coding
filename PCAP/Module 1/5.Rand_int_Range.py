'''
The randrange and randint functions

If you want integer random values, one of the following functions would fit better:

randrange(end)
randrange(beg, end)
randrange(beg, end, step)
randint(left, right)
'''

print("--------------------------Rand-Range-----------------------")

from random import randrange

#Generate a random number between 0-9
ran_1 = randrange(10)
print(ran_1)


#first is starting, second is ending, third is step
ran_even = randrange(10,20,2)
print(ran_even)

print("--------------------------generating between -100 to 0-----------------------")

ran_negative = randrange(-100, 0)
print(ran_negative)
#from -100 to -1 cuz 0 is not included

print("--------------------------Intersting-Random----------------------")

print(randrange(1))
print(randrange(0,1))
print(randrange(0,1,1))



print("--------------------------Rand-int-----------------------")
#Randint includes the last number also
from random import randint

print(randint(0,1))



print("--------------------------Rand-int-repitition----------------------")

for i in range(10):
    print(randint(1,10), end=",")

#There is a issue we can get the same value more than once.

print("--------------------------Rand-int-Remove-repitition----------------------")


