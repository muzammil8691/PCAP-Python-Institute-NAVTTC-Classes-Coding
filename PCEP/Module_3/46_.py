Q1="the_____is defined as a weakness or flaws in the design,implementation or behaviours of a systm or application"
user=input(Q1)
if user=="vulnerability":
    print("correct")
else: 
    for i in range(1):
        Again=input("wrong,do u want the same question again (yes/no)")
    if Again=="yes":
        print(input(Q1))
        if user=="vulnerability":
            print("correct")
        else:
            print("Exit")
            print("The right answer is: vulnerability")
            
    
Q2="A_____is something such as an action or behaviour that utilize a vulnerability on a system or  application"
Q2user=input(Q2)
if user=="exploit":
    print("correct")
else:
   for i in range(1):
        Again=input("wrong,do u want the same question again (yes/no)")
        if Again=="yes":
            print(input(Q2))
            if Q2user=="exploit":
                print("correct")
                        
            else:
                print("the right answer is:Exploit")
        else:
            break