
#Error in code

largest_number = -9999999999

while True:
    number = int(input("Enter a number to compare: "))
    if number == "-1":
        break

    elif number > largest_number:
         
            largest_number = number
            number = int(input("Enter another number to compare or press '-1' to exit: "))

print(largest_number)