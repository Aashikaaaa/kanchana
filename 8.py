'''Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers should be printed on the output screen. 
Also try the same program by replacing 2000 and 3200 by taking input for them from the users.
'''
def find_numbers (start, end):
    result = []
    for num in range(start, end + 1):
        if num % 7 == 0 and num * 5 != 0: 
            result.append(num)
    return(result)

print (find_numbers (2000, 3200))

start = int(input("Enter the starting number: "))

end=int (input("Enter the ending number: "))

print("Number between {} and {} that are divisible by 7 but not a multiple of 5: ".format(start, end))
print (find_numbers (start, end))