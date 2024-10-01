#testing the function result with pre-defined data (Testing)

def is_year_leap(year):
#
    if year >= 1582:
        if year % 4 != 0:
            return False  # Not Leap
        elif year % 100 != 0:
            return True  # Leap Year
        elif year % 400 == 0:
            return True  # Leap Year
        else:
            return False  # Not Leap
    else:
        return None  # Not in Calendar

test_data = [1900, 2000, 2016, 1987]

test_results = [False, True, True, False]


for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
     
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
