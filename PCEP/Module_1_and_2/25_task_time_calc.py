hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.


mins = mins + dura

hour_new = mins//60  #Converts min to hours using floor div

hour = hour + hour_new

hour = hour%24 #format hours 0-23

mins = mins%60 #format min to 0-59

print(hour, ":", mins)