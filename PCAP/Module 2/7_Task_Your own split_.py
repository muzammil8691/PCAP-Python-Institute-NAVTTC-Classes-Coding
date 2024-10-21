def mysplit(strng):
    lst = []
    x = ''
    for i in strng:
        if i != " ":
            x += i
        elif i == " ":
            if x != "":
                lst.append(x)
                x = ""
    if x:  # To add the last word if there's no trailing space
        lst.append(x)
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
