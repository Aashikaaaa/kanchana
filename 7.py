'''Write a program to display the prime number between 2 numbers input by the users.
 Also print the sum of all the prime numbers. [Hint: Prime numbers are the one which are
 either divisible by 1 or themselves. 3, 5, 7, 11, etc are some of the examples.]'''
def prime_number (num):
    for i in range(2, int (num**0.5)+1):
        if num % i == 0:
            return False
    return True
def sum_of_prime_number (start, end):
    prime_numbers = []
    prime_numbers_sum = 0

    for num in range(start, end):
        if prime_number (num):
           prime_numbers.append(num)  
           prime_numbers_sum = prime_numbers_sum + num
        print("Prime number between {start} and {end} are: {prime_numbers}")
        print("Sum of prime numbers: ",prime_numbers_sum)
        
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum_of_prime_number (start, end)