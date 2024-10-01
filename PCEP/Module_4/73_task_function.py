#Task
'''
Write a function called display_message() that prints one sentence 
telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly
'''



def display_message():
      """Display a message about chapter""" #docstring

      print("We are learning about functions in this chapter. i.e., how to create and use them.")



display_message()


#Task 2

'''Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call.
'''

def favourite_book(title):
    """Display a book name using parameter""" #docstring
    
    print(f"one of my Favourite Book is {title.title()}")


favourite_book("aLice in wonDerland")
favourite_book("Python 3")

      