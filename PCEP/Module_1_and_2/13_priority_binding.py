'''
Priority and Binding rules from W3 Schools
'''


#Division and answer
print(100 / 5 * 3)

#According to rule the operation will be from left to right that gives 20.0 
#because division always gives float value and 20.0 multiply by 3 is 60.0







#ANother
print(9 % 6 % 2)    ##the modulo operator uses left-sided binding

print(2 ** 2 ** 3)  #the exponentiation operator uses right-sided binding. (exception)

'''
It gives answer = 256
why?
cuz in exponent we go from right to left but with a trick
 firstly, 2**3 which is 8
then, 2 ** 8 which gives 256
'''

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)