import csv

# Function to calculate the average score for a student
def calculate_average(scores):
    return sum(scores) / len(scores)

# Initialize a dictionary to store student names and their average scores
student_averages = {}

# Read the data from the "student_grades.csv" file
with open("student_grades.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in reader:
        name = row["Name"]
        math_score = float(row["Maths"])
        science_score = float(row["Science"])
        english_score = float(row["English"])
        
        # Calculate the average score for the student
        average_score = calculate_average([math_score, science_score, english_score])
        
        # Store the student's name and their average score in the dictionary
        student_averages[name] = average_score

# Write the data to a new CSV file "student_average_grades.csv"
with open("student_average_grades.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Average"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the student names and their average scores
    for name, average_score in student_averages.items():
        writer.writerow({"Name": name, "Average": average_score})

print("Average scores have been calculated and saved to 'student_average_grades.csv'")
