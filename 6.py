'''Write a program to input the number of 5 subjects from the user, 
calculate the average, total, percentage and division of the students on
 the basis of specifications mentioned below.
I.	If the percentage value is 80 or above, the user obtains distinction.
II.	If the percentage is above 60, the user obtains first division.
III.	If the percentage is above 50, the user obtains second division.
IV.	If the percentage is above 45, the user obtains third division.
V.	If the percentage is below 45, the user obtains fail division.
'''
# Function to calculate the division based on the percentage
def calculate_division(percentage):
    if percentage >= 80:
        return "Distinction"
    elif percentage >= 60:
        return "First Division"
    elif percentage >= 50:
        return "Second Division"
    elif percentage >= 45:
        return "Third Division"
    else:
        return "Fail Division"

# Input for 5 subjects
subject_marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    subject_marks.append(mark)

# Calculate total and average
total_marks = sum(subject_marks)
average_marks = total_marks / 5

# Calculate percentage
percentage = (total_marks / (5 * 100)) * 100

# Display results
print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage}%")
print("Division:", calculate_division(percentage))
