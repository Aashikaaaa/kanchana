'''Write a program to find the sum of odd and even numbers input from the user.
The program should take an input continuously until the user wants to exit the program.
The program should be menu driven where the user should be asked whether they want to
continue with the program or not.'''
def sum_odd_even_numbers():
    odd_sum = 0
    even_sum = 0

    while True:
        print("\nMenu:")
        print("1. Enter a number")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                even_sum += number
            else:
                odd_sum += number
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    return odd_sum, even_sum

# Main program
print("This program calculates the sum of odd and even numbers.")
odd_total, even_total = sum_odd_even_numbers()
print("\nSum of odd numbers:", odd_total)
print("Sum of even numbers:", even_total)
print("Exiting the program. Goodbye!")
