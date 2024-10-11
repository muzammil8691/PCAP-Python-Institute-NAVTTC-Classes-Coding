import sys

for p in sys.path:
    print(p)

#All the path in current directory


from sys import path



#if the file which has to be impoted is not in the current directory you can locate the file like this to import it. 
path.append('..\\module_three')

import module_three

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module_three.suml(zeroes))
print(module_three.prodl(ones))

