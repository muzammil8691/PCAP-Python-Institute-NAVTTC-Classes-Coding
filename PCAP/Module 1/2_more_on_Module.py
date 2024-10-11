print("---------------------------import-module-with-User-Defined-Name------------------")

import math as m
print(m.sin(90))


print("---------------------------import-Specific-function-with-User-Defined-Name------------------")

from  math import radians as rad

ad = 90
ar =rad(ad)
print(ar)



print("---------------------------import-and-Dir-----------------")

from  math import radians

# print(dir(math))
#It will throw a error 


print("---------------------------import-e-constant----------------")

from math import e

print(e)            #e is constant 2.71
print(pow(e,2))     #Power of e as 2



# import math Module: e → a constant with a value that is an approximation of Euler's number (e)

# exp(x) → finding the value of ex;

# log(x) → the natural logarithm of x

# log(x, b) → the logarithm of x to base b

# log10(x) → the decimal logarithm of x (more precise than log(x, 10))

# log2(x) → the binary logarithm of x (more precise than log(x, 2))


#-----------------------------------------------------------------------#



# The last group consists of some general-purpose functions like:

print("---------------------------import-Ceil----------------")
# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
from math import ceil
print(ceil(10.2)) 

print("---------------------------import-floor----------------")
# floor(x) → the floor of x (the largest integer less than or equal to x)
from math import floor
print(floor(12.9))


print("---------------------------import-Trunc----------------")
# trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
from math import trunc
print(trunc(15.3))

print("---------------------------import-Factorial----------------")
# factorial(x) → returns x! (x has to be an integral and not a negative)
from math import factorial
print(factorial(5))

print("---------------------------import-Factorial----------------")
# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)

from math import hypot
print(hypot(5,4))

