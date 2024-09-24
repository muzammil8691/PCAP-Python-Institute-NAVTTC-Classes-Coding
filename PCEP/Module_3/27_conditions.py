#All about identation on if statements

x = int(input("Enter a integer value:"))

if x<10:
    print(f"The number {x} is less than 10")
    print("hello")
#this code works when x<10

if x<10:
    print(f"The number {x} is less than 10")
print("hello")    
#if x>10 only print hello will work & if x<10 both will work
