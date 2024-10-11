'''
Is there real randomness in computers?
Another module worth mentioning is the one named random.

It delivers some mechanisms allowing you to operate with pseudorandom numbers.
psedurandom means false random.
'''

#We use the seed() method to give starting value of random. By default it takes the current computer time.
print("-------------------------Random-Default------------------------")
from random import random

for i in range(5):
    print(random())
#produces a float number x coming from the range (0.0, 1.0) by default - in other words: (0.0 <= x < 1.0).

print("-------------------------Using-Seed------------------------")


from random import random, seed

seed(5)
for i in range(5):
    print(random())




