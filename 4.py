'''Write a program to take a number input from the user and display the
 result of some mathematical calculations as mentioned below.
I.	Square of the number
II.	Square root of the number
III.	Exponent value with the number
IV.	Log Base 10 of the number
V.	Calculate the power 3, 4 and 5 of the number.
'''
# function to calculate the square of a number
def square_number(num):
    return num ** 2

# function to calculate the square root of a number
def square_root_number(num):
    return num ** 0.5

# function to calculate the exponentiation of a number
def exponent(num, exponent):
    return num ** exponent

# Ask user to enter a number
number = float(input("Enter a number: "))

# Calculate the powers of the number for exponents 3, 4, and 5
power_3 = number ** 3
power_4 = number ** 4
power_5 = number ** 5

# Ask user to enter an exponent value
exponent_value = int(input("Enter the exponent value: "))

# Calculate the square and square root of the input number
square = square_number(number)
square_root = square_root_number(number)

# Print the results
print(f"Square number of {number} is: {square}")
print(f"Square root number of {number} is: {square_root}")
print(f"{number} raised to the power of 3 is: {power_3}")
print(f"{number} raised to the power of 4 is: {power_4}")
print(f"{number} raised to the power of 5 is: {power_5}")
