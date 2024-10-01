#Converting the Pound value to Kilos and Kilos to Pounds

def pound_to_kg(pound):
    #This function converts Pounds to Kgs #Docstring
    #1 pound = 0.45359237

    result = pound * 0.45359237
    return result

def kg_to_pound(kg):
    #This function converts kgs to Pounds #Docstring
    #1 kg = 2.20462

    result = kg*2.20462
    return result

print(pound_to_kg(20), "Kilograms")
print(kg_to_pound(42), "Pounds")