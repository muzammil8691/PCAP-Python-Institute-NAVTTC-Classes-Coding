
print("--------------------- L Strip ---------------------")
#Returns a left trim version of the string
#Remove spaces to the left of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")


#Removes '.', 'c', 'o', 'm' all characters starting from left 
#If found any other characters it stops immediately
print("cisco.com".lstrip(".com"))     #Result: cis


print("--------------------- R Strip ---------------------")
#Returns a right trim version of the string
#Remove any white spaces at the end of the string
txt = "     banana     "
x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#Removes '.', 'c', 'o', 'm' all characters starting from right 
#If found any other characters it stops immediately
print("cisco.com".rstrip(".com"))     #Result: cis


print("--------------------- Strip ---------------------")
#Returns a trimmed version of the string
#Remove spaces at the beginning and at the end of the string
txt = "     banana     "
x = txt.strip()

print("of all fruits", x, "is my favorite")


#Removes '.', 'c', 'o', 'm' all characters from string
#If found any other characters it doesn't stop 
print("cisco.com".strip(".com"))     #Result: cis


