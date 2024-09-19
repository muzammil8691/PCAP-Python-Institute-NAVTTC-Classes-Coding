kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#If we dont have to round off. Instead we have to floor and ceal then we use import

import math
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", math.ceil(miles_to_kilometers), "kilometers")
print(kilometers, "kilometers is", math.floor(kilometers_to_miles), "miles")