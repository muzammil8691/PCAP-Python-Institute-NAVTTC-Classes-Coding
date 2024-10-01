secret_number = 777

number = int(input("Guess the Secret Number: "))

while number != secret_number:
    print("Ha ha! You're stuck in my loop!\n")

    number = int(input("Guess the Secret Number Again: "))
else:
    print("Well done, muggle! You are free now.")

