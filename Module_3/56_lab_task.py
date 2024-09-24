
hat_list = [1,2,3,4,5]

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.


user = int(input("Please Enter a Number: "))

hat_list[2] = user
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
