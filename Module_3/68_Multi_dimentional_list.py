# 3.7.1.1 Multi Dimentional Lists
#List in List

#-------------------------------------------------------------------#
#Traditional Method
board = []
row = []
for i in range(3):
  row.append("E")
for j in range(3):
  board.append(row)
print(board)

board[1][1] = 'X'
print(board)


#-------------------------------------------------------------------#
## List Comphrension
board = []

for i in range(3):
    row = ["E" for i in range(3)]
    board.append(row)
print(board)

#Changing the value at any index
board[1][1] = 'X'
print(board)


#-------------------------------------------------------------------#
### List Comphrension
board = [["E" for i in range(3)] for i in range(3)]
print(board)

#Changing the value at any index

board[0][0] = 'M'
board[0][1] = 'U'
board[0][2] = 'Z'
print(board)
print(board[1])



