
zero = ['###', '# #', '# #', '# #', '###']
one = ['  #', '  #', '  #', '  #', '  #']
two = ['###', '  #', '###', '#  ', '###']
three = ['###', '  #', '###', '  #', '###']
four = ['# #', '# #', '###', '  #', '  #']
five = ['###', '#  ', '###', '  #', '###']
six = ['###', '#  ', '###', '# #', '###']
seven = ['###', '  #', '  #', '  #', '  #']
eight = ['###', '# #', '###', '# #', '###']
nine = ['###', '# #', '###', '  #', '###']

display = []

user = input("Enter numbers to display: ")

#Apeending each list according to user input
for i in user:
    if i == '0':
        display.append(zero)
    if i == '1':
        display.append(one)
    if i == '2':
        display.append(two)
    if i == '3':
        display.append(three)
    if i == '4':
        display.append(four)
    if i == '5':
        display.append(five)
    if i == '6':
        display.append(six)
    if i == '7':
        display.append(seven)
    if i == '8':
        display.append(eight)
    if i == '9':
        display.append(nine)


#Displaying each index of each row
for row in range(5):
    for num in display:
        print(num[row], end="  ")
    print()
