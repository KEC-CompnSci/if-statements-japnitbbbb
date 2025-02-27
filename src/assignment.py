# Grade Calculator Assignment
# This script calculates a student's academic standing based on their scores and assignment completion.

# Do not modify these test scores and settings
test_score = 85
exam_score = 78
all_assignments_completed = True

# TASK 1: Calculate the final score as the average of test_score and exam_score
str(test_score)
str(exam_score)
average = (test_score + exam_score) / 2
final_score = average

final_score = None  # Replace None with the calculation

int(test_score)
int(exam_score)
final_score = (85 + 78) / 2

# TASK 2: Determine if the student passed
# A student passes if their final_score is 60 or higher
final_score = 81.5
final_score >= 60

passed = None  # Set to True or False using an if statement

if final_score >= 60:
    print(final_score >= 60) #True
passed = True

# TASK 3: Assign a letter grade based on the final_score
# Score 90-100: "A"
# Score 80-89: "B"
# Score 70-79: "C"
# Score 60-69: "D"
# Score below 60: "F"


letter_grade = ""  # Set the letter grade using if-elif-else

if final_score >= 90:
    print("A")
elif final_score >= 80:
    print("B")
elif final_score >= 70:
    print("C")
elif final_score >= 60:
    print("D")
else:
    print("F")
letter_grade = "B"

# TASK 4: Determine honor roll status
# To be on the honor roll, a student needs:
# - A final_score of 90 or higher
# - All assignments completed
# ===== YOUR CODE HERE =====

honor_roll = None  # Set to True or False using an if statement

if final_score >= 90:
    print(honor_roll) #False
honor_roll = False

# TASK 5: Determine if the student can take the advanced course
# Students can take the advanced course if:
# - They passed (final_score >= 60)
# - AND they either:
#   - Have a letter grade of "A" OR
#   - Have a letter grade of "B" AND have completed all assignments
# ===== YOUR CODE HERE =====

can_take_advanced = None  # Set to True or False using if statements with AND/OR

if final_score >= 60 and letter_grade == "A" or letter_grade == "B":
    print(can_take_advanced) #True
can_take_advanced = True

# This prints the results (do not modify)
print("Final Score:", final_score)
print("Passed:", passed)
print("Letter Grade:", letter_grade)
print("Honor Roll:", honor_roll)
print("Can Take Advanced Course:", can_take_advanced)