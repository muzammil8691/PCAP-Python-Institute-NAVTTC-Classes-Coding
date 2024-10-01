#4.6.1.12 SECTION SUMMARY (3/3)

tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

print()
print("#----------------------------First-Method-----------------------------------#")
print()
#Complete the code to correctly use the count()
# method to find the number of duplicates of 2 in the following tuple.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = 0
for i in tup:
    if i == 2:
        duplicates += 1 

print("Duplicates are: ",duplicates)

print()
print("#-----------------------------Second-Method----------------------------------#")
print()

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print("Duplicates are: ",duplicates)


print()
print("#---------------------------Glue-in-d3-----------------------------------#")
print()
#Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # Write your code here.
    for i in (d1, d2):
        d3.update(i)
print(d3)

print()
print("#---------------------------convert-list-into-tuple--------------------------------#")
print()
#Write a program that will convert the my_list list to a tuple.

my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)

print()
print("#---------------------------convert-tuple-into-dictionary--------------------------------#")
print()
#Write a program that will convert the colors tuple to a dictionary.

colors = (("green", "#008000"), ("blue", "#0000FF"))
#tuple witin tuple the pair acts as key and value
# Write your code here.
for i in colors:
    colors_dictionary = dict(colors)

print(colors_dictionary)

print()
print("#---------------------------Analyze-what-happens-------------------------------#")
print()

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)

print()
print("#---------------------------accessing-the-key-value-for-loop--------------------------#")
print()

colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)



