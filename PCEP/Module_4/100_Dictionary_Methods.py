#Methods used with dictionary

#-----------------------Printing-Values-from-Dictionary--------------------------------#

my_dict = {"name": "Alice", "age": 30, "city": "New York", "profession": "Engineer"}

for key in my_dict.keys():
    print(key, "-->", my_dict[key])



#---------------------------Printing-Sorted-Values-from-Dictionary-------------------------------#

print("__________Sorted_Dictionary__________")
my_dict = {"name": "Alice", "age": 30, "city": "New York", "profession": "Engineer"}

for key in sorted(my_dict.keys()):
    print(key, "-->", my_dict[key])

#in sorting if first letter is capital it doesn't matter it is "Z" it will come first.
#Capital "Z" comes first from Small "z"


#-----------------------------------Printing-Items-from-Dictionary----------------------------------------#

print("__________Items_Dictionary__________")

my_dict = {"name": "Alice", "age": 30, "city": "New York", "profession": "Engineer"}

for items in my_dict.items():
    print(items)

#-----------------------------------Printing-values-from-Dictionary----------------------------------------#


print("__________Values_Dictionary__________")

my_dict = {"name": "Alice", "age": 30, "city": "New York", "profession": "Engineer"}

for values in my_dict.values():
    print(values)
