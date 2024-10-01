#The dictionary is another Python data structure. 
#It's not a sequence type (but can be easily adapted
#to sequence processing) and it is mutable

#----------------------------------------------------------#
#How to create a dictionary
#Key : Value

my_dictionary = {"Brand": "Ford", "Model": "Mustang", "Year": 1964}

print(my_dictionary)
print(my_dictionary["Brand"])

my_dictionary_2 = {1: "Apple", 2: "Ball", 3: "Cat"}
print(my_dictionary_2)
print(my_dictionary_2[1]) #here 1 is key not the index


#----------------------------------------------------------#
#Playing with Dictionary 

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["colors"])
print(thisdict["colors"][0])


#----------------------------------------------------------#
#keys keyword in dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

#----------------------------------------------------------#
#values keyword in dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)






