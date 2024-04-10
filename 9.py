'''Write a program to find the factorial of any number taken as an input from the user.
Try to validate the user input whether it is a number or not and then only perform the operation.
In case of other than number as an input, display an error as “Not a number.”.
[Hint: few available functions to identify the input is a number or not are 
‘isdigit(), isnumeric(), etc.]'''
def factorial(n):
    if n==0:
      return 1

    else:
      return n*factorial (n-1)

user_input = input("Enter the number to find its factorial: ")
if user_input.isdigit: # isdigit check whether all character are digit or not if not it return false
   num = int(user_input)
   if num < 0:
      print("Factorial is not defined for nehative numbers.")
   else:
       print (f"The factorial of {num} is {factorial (num)}.")

else:
    print("Error: Not a number.")