#Task to be done

rooms = [[[False for r in range(2)] for f in range(4)] for t in range(3)]
print(rooms)






# rooms[1][0][1]= True
# print(rooms[1][0][1])
# print(rooms)
print()
print("-------------------Converting List Comphrension into Traditional Method--------------------")
print()

room = []
floor = []
block = []

for r in range(2):
    room.append(False)
for f in range(4):
    floor.append(room)
for t in range(3):
    block.append(floor)

print(block)

