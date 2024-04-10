'''Solve the below mentioned expressions in a python program. 
Feel free to take input of the required variables to solve the expressions. 
I.	a2 + 2ab + b2
II.	a5 + 2abc + b3 + c4
III.	a7 + 5a3b2c6 + b7
'''
# function to calculate the result of the expression a^2 + 2ab + b^2
def expression_result(a, b):
    result = a**2 + 2*a*b + b**2
    return result

# function to calculate the result of the expression a^7 + 2abc + b^3 + c^4
def expression1_result(a, b, c):
    result1 = a**7 + 2*a*b*c + b**3 + c**4
    return result1

# function to calculate the result of the expression a^7 + 5a^3b^2c^6 + c^7
def expression3_result(a, b, c):
    result3 = a**7 + 5*a**3*b**2*c**6 + c**7
    return result3

# Ask user to enter values for a, b, and c
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))

# Calculate the result of each expression by calling the respective functions
result = expression_result(a, b)
result1 = expression1_result(a, b, c)
result3 = expression3_result(a, b, c)

# Print the results
print("The result of the expression a^2 + 2ab + b^2 is:", result)
print("The result of the expression a^7 + 2abc + b^3 + c^4 is:", result1)
print("The result of the expression a^7 + 5a^3b^2c^6 + c^7 is:", result3)
