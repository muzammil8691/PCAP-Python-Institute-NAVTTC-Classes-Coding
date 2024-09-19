from datetime import date

#To fetch Date 
today = date.today()

print("Today's Date is: ",today)



#To Format the Date


#%Y for year
#%m for month
#%d for day
#%B for month as a name
#%D show full date in slashes 23/6/2000

format= today.strftime('%d %B, %Y')
print(format)


#To display Week Day

weekday= today.weekday()
print(weekday)

if(weekday == 1):
    print("Monday")
elif(weekday == 2):
    print("Tuesday")
elif(weekday == 3):
    print("Wednesday")


#To get difference between two dates in number of days
f_date = date(2000, 12, 25)

l_date = date(2024, 3, 21)

difference = l_date - f_date
print(difference.days)