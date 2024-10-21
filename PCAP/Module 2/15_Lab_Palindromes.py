#2.5.1.7 LAB: Palindromes


def palindrome(str):
   str = str.replace(" ", '')
   str = str.lower()

   reverse = str[::-1]

   if str == reverse:
      return "Palindrome"
   else:
      return "Not Palindrome"

str = 'Ten animals I slam in a net'
print(palindrome(str))
