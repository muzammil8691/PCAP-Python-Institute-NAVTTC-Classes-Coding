"""
14/3/2024
This program is to find average speed

"""

d = int(input("Input the distance in Km's: ")) #d is distnace in Kilometers
t = int(input("input the time in Hours: ")) #t is time in Hours

s = d//t #s is speed
print("The average speed of the car is",s, "Km/hr")

#The double back slash means only integer will be considered

'''
print("The average speed of the car is",round(s), "Km/hr")
'''
#round() means the number will be rounded off
