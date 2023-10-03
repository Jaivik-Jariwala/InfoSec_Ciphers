def combine_student_data(file_names, output_file):
    try:
        with open(output_file, "w") as output_f:
            for file_name in file_names:
                with open(file_name, "r") as input_f:
                    student_data = input_f.read()
                    output_f.write(student_data)
                    output_f.write("\n")  # Add a newline after each student's data

        print("Data of all students has been combined into 'Achievement.txt'.")

    except FileNotFoundError:
        print("Error: File not found")
    except IOError:
        print("Error: Input/Output error")

# List of individual student file names
student_files = ["student1.txt", "student2.txt", "student3.txt", "student4.txt"]

# Output file name
output_file_name = "Achievement.txt"

# Call the function to combine the data
combine_student_data(student_files, output_file_name)
'''
Function Documentation: combine_student_data

This function takes a list of individual student data file names and combines their data into a single output file named "Achievement.txt".

Parameters:

file_names (list of str): A list containing the names of individual student data files to be combined.
output_file (str): The name of the output file where the combined data will be written.
Returns:

None
Output:

The function will create a new file named "Achievement.txt" and write the combined data of all students into it.
Files:

combine_student_data.py: The Python script containing the implementation of the combine_student_data function.
student1.txt, student2.txt, student3.txt, student4.txt: Individual student data files containing name, ID number, branch, and achievement.
Achievement.txt: The output file where the combined data of all students will be written.
'''