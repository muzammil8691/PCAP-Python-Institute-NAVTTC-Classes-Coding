#Passing Information to a Function
'''
Types of Parameter
1. Positional Parameter
2. Keyword Parameter
3. Default Parameter
'''

def greet_user(username):   #Parameters
  """Display a simple greeting."""
  print(f"Hello, {username.title()}!")
  print(f"Hello, {username.upper()}!")

greet_user('ihsan')



#Function may or may not return anything
def addition(a,b):
  c = a+b
  return c

addition(5,5)