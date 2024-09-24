weather_is_fine = input("is weather Good or Bad?")


tickets = False

if weather_is_fine == "good":
    print("Let's go for a walk")
    find_nice_restaurant = input("Nice Restaurant found or not?")
    if find_nice_restaurant == "yes":
        print("Have a Lunch")
    else:
        print("Eat a Sandwich")
else:
    print("Go to theatre")
    tickets = input("Tickets available or not?")
    if tickets == "yes":
        print("Watch movie")
    else:
        print("Go for Shopping")
            
