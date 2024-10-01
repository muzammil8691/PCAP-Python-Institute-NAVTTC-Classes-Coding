#recursion is a technique where a function invokes itself.

#Yes, there is a little risk indeed. If you forget to consider
#the conditions which can stop the chain of recursive invocations,
#the program may enter an infinite loop. You have to be careful

#-------------------------------------------------------#

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
#-------------------------------------------------------#
# This one is good
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)



#-------------------------------------------------------#
#recursion Summary Question

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))