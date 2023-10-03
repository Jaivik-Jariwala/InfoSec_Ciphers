num1 = int(input("Enter your marks: "))
num2 = int(input("Enter your marks: "))
num3 = int(input("Enter your marks: "))

# Dictionary to store grade points for each grade
grades_dict = {
    "O grade": 10,
    "A+ grade": 9,
    "A grade": 8,
    "B+ grade": 7,
    "B grade": 6,
    "Fail": 0
}

# List of credits for each subject
credits = [3, 2, 2]

# List to store points for each subject
points = []

# List of marks for each subject
marks = [num1, num2, num3]

# Calculate the points for each subject based on the marks
for mark in marks:
    if mark >= 80:
        points.append(grades_dict["O grade"])
    elif 70 <= mark < 80:
        points.append(grades_dict["A+ grade"])
    elif 60 <= mark < 70:
        points.append(grades_dict["A grade"])
    elif 50 <= mark < 60:
        points.append(grades_dict["B+ grade"])
    elif 40 <= mark < 50:
        points.append(grades_dict["B grade"])
    else:
        points.append(grades_dict["Fail"])

# Calculate the total credit points and total credits
total_credit_points = sum([credit * point for credit, point in zip(credits, points)])
total_credits = sum(credits)

# Calculate the GPA
gpa = total_credit_points / total_credits

print("Your GPA is:", gpa)
