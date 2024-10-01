def hello(name):    
    print("Hello,", name)    


name = input("Enter your name: ")

hello(name)    

#-----------------------Same-Code-Different-Method------------------------------#

def hello(name):
    print("Hello,", name)


first_name = input("Enter your name: ")

hello(first_name) 


#-------------------------Keyword-Argument-Passing------------------------------#
#Now position of argument doesn't matter

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Bond", first_name = "James")