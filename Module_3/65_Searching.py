lst = [1,2,3,4,5,6,7,8,9]

user = int(input("Which number you want to search: "))
search = True
while search:    
    for i in range(len(lst)):
        if user == i:
            print("Number found:",i, "at index", lst[i])
            search=False
