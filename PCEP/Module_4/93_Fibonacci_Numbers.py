# for 1 and 2 it gives  1 so fix it
# for greater values use the index and plus the sum in it 

#--------------------------------------------------------#
def fibonacci(x):
    if x < 1:
        return None
    if x < 3:
        return 1
    
    
    num1 = num2 = 1
    sum = 0

    for i in range(3, x+1):

        sum = num1 + num2
        num1, num2 = num2, sum
    return sum

#--------------------------------------------------------#

###fibonacci series
def fib(n):

    if n <0:
        return None
    
    list = [0,1]
    for i in range(2, n):
        next_term = list[-1] + list[-2]
        list.append(next_term)
    return list
x = fib(10)
print(x)
#--------------------------------------------------------#

for n in range(1, 10):
    print(fibonacci(n))