beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("List content: ", beatles)

for i in range(2):
    user = input("Enter the name to add: ")
    beatles.append(user)

print("List content after for loop: ", beatles)

del beatles[-1]
del beatles[-1]
print("List content after deleting: ", beatles)



beatles.insert(0, "Ringo Starr")

print("List content after inserting at index 0: ", beatles)
print("The Fab", len(beatles))
