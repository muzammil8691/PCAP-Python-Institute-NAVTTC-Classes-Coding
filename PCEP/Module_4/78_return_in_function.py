#Using Return in Function

import time
def happy_new_year(wishes = True):
    time.sleep(1)
    print("Three...")
    time.sleep(1)
    print("Two...")
    time.sleep(1)
    print("One...")
    time.sleep(1)

    if not wishes:
        return
    
    print("Happy New Year")

happy_new_year()

happy_new_year(False)


#----------------------None-in-Function---------------------------#

value = None
if value is None:
    print("Sorry, you don't carry any value")


######

def strange_function(n):
    if n%2 == 0:
        return True

print(strange_function(2))
print(strange_function(1))
 

