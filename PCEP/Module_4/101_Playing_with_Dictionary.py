#Replacing the value from dictionary


laptop_specs = {"brand": "Lenovo", "model": "V14", "processor": "Intel i5", "ram": "16GB"}

laptop_specs["ram"] = "8GB"

print(laptop_specs)

print(laptop_specs["ram"])

#this method can also be used to add another key value pair as well as to replace a specific value


#------------------------------Deleting-item-from-Dictionary---------------------------------#

print("___________________DELETE_Item__________________")

car = {"brand": "Corolla", "model": "GLI", "year": "2009"}

del car["year"]
print(car)

#------------------------------Pop-item-from-Dictionary---------------------------------#

print("___________________POP_Item___________________")

car = {"brand": "Corolla", "model": "GLI", "year": "2009"}

car.popitem()
print(car)


#------------------------------Accessing-item-from-Dictionary---------------------------------#

print("___________________Accessing_Item___________________")

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

print(pol_eng_dictionary["gleba"])    # outputs: soil


print(pol_eng_dictionary.get("woda"))    # outputs: water




#------------------------------Copying-Dictionary---------------------------------#

print("___________________Copying_Dictionary__________________")

dict = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }


a = dict.copy()

print(dict)
print(a)