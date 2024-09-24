income = float(input("Enter your annual income: "))


if income <= 85528:
    tax = income/100 * 18
    tax = tax - 556.02

    if tax < 0:
        print("Your Tax is Zero")
    else:
        print(f"Your Payable tax Amount is {round(tax)}")
else:
    tax = income - 85528
    tax = tax/100 * 32
    tax = tax + 14839.02
    
    print(f"Your Payable tax Amount is {round(tax)}")