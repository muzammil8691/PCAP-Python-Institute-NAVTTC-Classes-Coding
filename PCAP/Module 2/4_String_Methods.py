print("---------------------Ends With ---------------------")
#Gives True or False based on argument given 
txt = "Muzammil"
print(txt.endswith("l"))     #True

print("--------------------- Starts With ---------------------")
#Gives True or False based on argument given 
txt = "Muzammil"
print(txt.startswith("u"))   #False

print("--------------------- is alum ---------------------")
# Checks if given string has only numbers and characters.
print('lambda30'.isalnum())     #True
print('lambda'.isalnum())       #True
print('30'.isalnum())           #True
print('@'.isalnum())            #False
print('lambda_30'.isalnum())    #False
print(''.isalnum())             #False


print("--------------------- is alpha ---------------------")
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())            #True   
print('Mu40'.isalpha())             #False

print("--------------------- is digit ---------------------")
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())             #True
print("Year2019".isdigit())         #False

print("--------------------- is lower ---------------------")
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())            #False
print('moooo'.islower())            #True

print("--------------------- is space ---------------------")
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())             #True
print(" ".isspace())                #True
print("mooo mooo mooo".isspace())   #False

print("--------------------- is upper ---------------------")
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())            #False
print('moooo'.isupper())            #False
print('MOOOO'.isupper())            #True