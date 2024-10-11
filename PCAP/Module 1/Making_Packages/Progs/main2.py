from sys import path
path.append('..\\Making_Packages')


import Extra.iota
print(Extra.iota.funI())

# or for going upto the fucntion

from sys import path
path.append('..\\Making_Packages')

from Extra.iota import funI
print(funI())


#Now let's reach all the way to the bottom of the tree

import Extra.Good_Packages.Best_Packages.sigma

from Extra.Good_Packages.Best_Packages.tau import funT


print(Extra.Good_Packages.Best_Packages.sigma.funS())
print(funT()) 


#You can make your life easier by using aliasing:

from sys import path

path.append('..\\Making_Packages')

import Extra.Good_Packages.Best_Packages.sigma as sig
import Extra.Good_Packages.alpha as alp

print(sig.funS())
print(alp.funA())

