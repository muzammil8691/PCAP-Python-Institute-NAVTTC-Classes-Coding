#A file containing Python definitions and statements.

import math
print(dir(math))


print("---------------------------Import-Module----------------------")

import math

ad = 90
ar =math.radians(ad)
print(ar)


print("---------------------------Import-Module-With-Function-Name--------------------")

from  math import radians

ad = 90
ar =radians(ad)
print(ar)


print("---------------------------Import-Specific-Functions---------------------")
#You can also import only the selected functions from a module.

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
###########

print("---------------------------import-Specific-Functions---------------------")

from math import e, exp, log

print(pow(e,1))
print(exp(log(e)))
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))





