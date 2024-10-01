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

def day_of_year(year, month, day):

     #DocString
     '''This function takes three values year, month and day
        if year is leap it checks the month if its and or not and days passed to give total days
    '''
     month = month -1
     total_days = day
     days = [31,0,31,30,31,30,31,31,30,31,30,31]
     
     if is_year_leap(year) is True:
        days[1] = 29
     elif is_year_leap(year) is False:
        days[1] = 28

     if month <1 or month > 12:
         return None
     if day > days[month] or day < 1:
         return None     
     for x in range(month):
         total_days += days[x]
         days[x] = days[x+1]
     return total_days
    
    
     
#Testing
print(day_of_year(1987, 6, 31))


