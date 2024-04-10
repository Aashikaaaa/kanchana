'''Write a program to input 2 numbers from the users and display the output of below mentioned operations in a proper format.
I.	Addition
II.	Subtraction
III.Multiplication
IV.	Division
V.	Modulo division
VI.	Floor division
'''


# Ask user to enter the first integer
a = int(input("Enter the first integer: "))
# Prompt the user to enter the second integer
b = int(input("Enter the second integer: "))

# addition
def addition(x, y):
    return x + y
# subtraction
def subtraction(x, y):
    return x - y
# multiplication
def multiplication(x, y):
    return x * y
# division
def division(x, y):
    return x / y
# modulo division
def modulo_division(x, y):
    return x % y
# floor division
def floor_division(x, y):
    return x // y
# addition 
add = addition(a, b)
# Print the result of addition
print("Addition between two integers is:", add)
# substraction
subtract = subtraction(a, b)
# Print the result of subtraction
print("Subtraction between two integers is:", subtract)
# multiplication
multiply = multiplication(a, b)
# Print the result of multiplication
print("Multiplication between two numbers is:", multiply)
# Division
divide = division(a, b)
# Print the result of division
print("Division between two integers is:", divide)
# Modulo Division
modulo = modulo_division(a, b)
# Print the result of modulo division
print("Modulo division between two integers is:", modulo)
# Floor Division
floor = floor_division(a, b)
# Print the result of floor division
print("Floor division between two integers is:", floor)

