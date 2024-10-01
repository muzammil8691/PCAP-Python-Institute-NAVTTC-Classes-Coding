#Task to be done

def is_year_leap(year):
    #DocString
    '''This function take a value 'Year' and returns True if its a Leap year 
       If its not a Leap year it return False 
    '''
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


def days_in_month(year, month):
     #DocString
     '''This function takes two values year and month
        if year is leap it checks the month and return days of that month and vice versa 
    '''
     if month <= 12 and month>0:

        if is_year_leap(year) is True and month == 2:
            return 29
        elif is_year_leap(year) is False and month == 2:
            return 28
        elif True:
            if month in [1,3,5,7,8,10,12]:
               return 31
            elif month in [4,6,9,11]:
               return 30
     else:
         return None


#Testing

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 4, 1, 11]
test_results = [28, 30, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
     
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")














#__________Trying Another_____________

        #old code with more lines


        #         if is_year_leap(year) is True:
        #     if month == 2:
        #        return 29
        #     elif month in [1,3,5,7,8,10,12]:
        #        return 31
        #     elif month in [4,6,9,11]:
        #        return 30
        # elif is_year_leap(year) is False:
        #     if month == 2:
        #        return 28
        #     elif month in [1,3,5,7,8,10,12]:
        #        return 31
        #     elif month in [4,6,9,11]:
        #        return 30