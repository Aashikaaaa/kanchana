""" Write a program to take a number input from the user and display
 whether the number is even or odd."""
# function to check if a number is even or odd
def even_or_odd(n):
    # Check if the number is divisible by 2
    if n % 2 == 0:
        # If the number is divisible by 2, it's even
        print('Even number')
    else:
        # If the number is not divisible by 2, it's odd
        print('Odd number')

# ask user to enter a number
num = int(input('Enter any number you like:'))

# Call the even_or_odd function with the input number
result = even_or_odd(num)

# Print the result of the function call
# Since the function doesn't return anything, result will be None
print(result)
