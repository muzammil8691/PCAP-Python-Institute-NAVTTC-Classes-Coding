question1 = "A _______ is defined as a weakness or flaw in the design, implementation or behaviors of a system or application. \n"
question2 = "An _______ is something such as an action or behavior that utilizes a vulnerability on a system or application. \n"


#Question1
answer = input(question1).strip().lower()

if answer == "vulnerability":
        print("Correct")
        print("Moving to the next question...")
else:
    for i in range(1):
        repeat = input("Do you want the same question again. Yes/No : ")
        if repeat == "yes":
            answer = input(question1).strip().lower()
            if answer == "vulnerability":
                print("Correct")
                print("Moving to the next question...")
        else:
            break

           

answer2 = input(question2).strip().lower()

if answer2 == "exploit":
        print("Correct")
else:
    for i in range(1):
        repeat = input("Do you want the same question again. Yes/No : ")
        if repeat == "yes":
            answer2 = input(question1)
            if answer2 == "exploit":
                print("Correct")
        else:
            exit()