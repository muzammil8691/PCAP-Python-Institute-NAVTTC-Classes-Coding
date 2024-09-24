#While Loop Method
'''
i =1 
while i<6:
   print(i)
   i += 1
else:
   print("The value you entered is not less than 6")
'''

#While Loop Method 2
i = 1
if i > 6:
   print("The value is greater than 6")
else:
   while i < 6:
      print(i)
      i += 1   

#Method 1

'''
prompt = "\nI will Repeat"
prompt += "\n Enter 'Q' to to end"

message = ""

while message != "Q":
    message = input(prompt)
    print(message)
'''
#Second Method

prompt = "\nI will Repeat"
prompt += "\n Enter 'Q' to to end"

flag = True

while flag:
    msg = input(prompt)
    if msg == "Q":
     print("Quitting...")
     flag = False
    else:
       print(msg)