'''
#BMI Calculator 
#Height of person in Meters
#Weight of person in Pounds
'''

def pound_to_kg(pound):
    #This function converts Pounds to Kgs #Docstring
    #1 pound = 0.45359237

    return pound * 0.45359237 
     

def feet_to_meters(feet, inches):
    #This function converts feet to meters #Docstring
    #1 feet = 0.3048 meters

    return feet * 0.3048 + inches * 0.0254
     

def bmi(kg, meter):
    #This function calculates BMI #Docstring

    return kg/meter**2
     


bmi_value = bmi(pound_to_kg(176), feet_to_meters(5, 7))

print(bmi_value)

if bmi_value < 16:
    print("Severe Thinness")
elif bmi_value >=16 and bmi_value <17:
    print("Moderate Thinness")
elif bmi_value >= 17 and bmi_value < 18.5:
    print("Mild Thinness")
elif bmi_value >= 18.5 and bmi_value < 25:
    print("Normal")
elif bmi_value >= 25 and bmi_value < 30:
    print("Overweight")
elif bmi_value >=30 and bmi_value < 35:
    print("Obese Class 1")
elif bmi_value >=35 and bmi_value < 40:
    print("Obese Class 2")
elif bmi_value >40:
    print("Obese Class 3") 