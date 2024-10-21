#2.5.1.9 LAB: The Digit of Life

'''Some say that the Digit of Life is a digit evaluated using somebody's birthday.
    It's simple - you just need to sum all the digits of the date.
    If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.
'''

user = input("Enter your Date of birth in Digits: ")

def digit_of_life(dob):
    digit = 0
    
    for number in dob:
        digit += int(number)

    while len(str(digit)) > 1:
        digit = digit_of_life(str(digit))

    else:
        return digit

print(f"Your Digit of Life is {digit_of_life(user)}")



