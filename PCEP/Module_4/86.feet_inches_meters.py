#Converting Feet and Inches into Metres
#1 feet = 0.3048 meters
#1 inch = 2.54 cm = 0.0254 m

def feet_to_meters(feet, inches):
    return feet * 0.3048 + inches * 0.0254


def inches_to_meters(inches):
    return inches * 0.0254


print(feet_to_meters(5, 9))
print(inches_to_meters(70.8))