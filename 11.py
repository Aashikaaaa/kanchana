'''Write a program to create a number guessing game for the user. The program should ask the user 
to input a number.The program specifications are as mentioned below.
I.	The program should generate a random number for the answer.
II.	The program should prompt the user for a number input.
III.The program should provide the feedback to the user after each guesses 
    (e.g. “Too high”, “Too low” or “Correct number”).
IV.	The program should check the user input for 5 times and allow the users to guess for at most
    5 times if their input don’t match the answer number.
V.	If the user is not able to guess the answer within 5 times, the program should display “Game Over” 
     message and exit.
'''
#Number guessing game
#random() → returns a random floating number between 0 and 1.
#uniform() + returns a random floating number between the two specified numbers (both included).
#randint() → returns a random integer number selected element from a range (both included) import random
import random 
print("Guess a number between 1 and 50")
a= random.randint(1,50)

for i in range(5):
    x = int(input("Enter any integer: "))
    if x >50:
       print("Invalid number. Please enter a Valid number")

    else:

      if x >a:
        print("Too High")

      elif x<a:
        print("Too low")

      elif x ==a:

        print("you win")
        break
      
print("Game Over")