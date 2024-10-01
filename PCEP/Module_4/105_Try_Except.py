print()
print("#---------------------------Try-Except-Branch----------------------------------#")
print()

try:
    value = int(input('Enter a natural number: '))
    print("You typed", value)
    print('The reciprocal of', value, 'is', 1/value)
except:
    print("You Entered the wrong Data")            
    

print()
print("#---------------------------Multiple-Except-1-------------------------------#")
print()

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 



print()
print("#---------------------------Multiple-Except-2-------------------------------#")
print()

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
    


print()
print("#---------------------------making-it-more-good-----------------------------#")
print()

decision = True
while decision:
    try:
        value = int(input('Enter a natural number: '))
        print('The reciprocal of', value, 'is', 1/value) 
        decision = False
    except ValueError:
       print('I do not know what to do.') 
       decision = True   
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.') 
        decision = True
    except:
        print('Something strange has happened here... Sorry!')


print()
print("#--------------------------Taking-Exception-from-Console---------------------------#")
print()

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value) 
       
except Exception as e:
       print(e) 

