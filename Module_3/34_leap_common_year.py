#Task 3.1.1.12      Common and Leap year 

year = int(input("Enter any Year: "))


if year >= 1582:
    if year%4 != 0:
        print("It's a Common Year")
    elif year%100 != 0:
        print("It's a Leap Year")
    elif year%400 !=0:
        print("It's a Common Year")
    else:
        print("It's a Leap year")
else:
    print("This Year doesn't comes under Gregorian Calendar")