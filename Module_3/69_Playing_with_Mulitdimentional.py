#Playing with Multi Dimentional Lists or list in list


regional_list =[
    ["UK", 'Spain'],
    ['Aus',"New"],
    ['Pak', 'Ind']
]
print(regional_list)
print(regional_list[1])
print(regional_list[1][1])

regional_list[2][1] = "China"
regional_list.append(["SA","WI"])



print(regional_list)
print(regional_list[1])
print(regional_list[2][1])