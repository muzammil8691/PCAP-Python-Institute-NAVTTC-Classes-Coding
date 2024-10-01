#Handling Exceptions

#try ----------> Put ambigious code.
#except--------> Exception is caugh here.
#else----------> It will run if no exception is thrown.
#finally-------> It will run no matter what.


def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as  e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Executed Successfully")

divide(10,2)

divide(10,0)

divide(10,"a")

