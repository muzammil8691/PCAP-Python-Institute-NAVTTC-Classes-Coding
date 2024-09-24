weather_is_fine = True
find_nice_restaurant = True

tickets = False

if weather_is_fine:
    print("Let's go for a walk")
    if find_nice_restaurant:
        print("Have a Lunch")
    else:
        print("Eat a Sandwich")
else:
    print("Go to theatre")
    if tickets == False:
        print("Go for Shopping")
            
