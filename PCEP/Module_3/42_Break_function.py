#Break Statement 



for i in range(1,11):
    if i == 6:
        break
    print("inisde the loop", i)
print("outside the loop", i)






#Break with for loop

import time

for i in range(1,11):
    time.sleep(1)
    if i == 6:
        break
    print("inisde the loop", i)
print("outside the loop", i)




