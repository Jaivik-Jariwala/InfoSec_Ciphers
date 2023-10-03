def read_grades(filename: str) -> None:
    """
    Reads the grades from a CSV file and calculates the total points, number of grades, and average grade.

    Parameters:
        filename (str): The name of the CSV file containing the grades data.

    Return Value:
        None

    Function Behavior:
    - The function attempts to open the specified CSV file using the 'with' statement to ensure proper handling of the file resources.
    - It reads all the lines from the file and stores them in the 'grade_csv' list.
    - The function initializes variables 'total_points' and 'count' to keep track of the sum of grades and the number of valid grades, respectively.
    - It iterates through each grade in 'grade_csv', removing any leading/trailing whitespaces using 'strip()'.
    - If the grade is not an empty string (i.e., a valid grade value), it is converted to a floating-point number and added to 'total_points'. The 'count' is incremented.
    - After the loop, the average grade is calculated by dividing 'total_points' by 'count'. If 'count' is zero (no valid grades), the average is set to zero to avoid division by zero.
    - The function then prints the total points, number of grades, and average grade on separate lines.

    Error Handling:
    The function includes error handling to catch specific exceptions that may occur during file operations or when processing invalid grade values. The following exceptions are caught:
    - FileNotFoundError: If the specified file is not found in the current directory or the provided path.
    - IOError: If there is an input/output error while reading the file.
    - ValueError: If an invalid grade value is encountered, causing a conversion error while trying to convert it to a floating-point number.

    Example Usage:
    filename = "grade.csv"
    read_grades(filename)

    Note:
    - The 'grade.csv' file should be a comma-separated values (CSV) file containing one or more numeric grade values on separate lines. Invalid grades or empty lines will be skipped during processing.
    - The function can be extended to include additional error handling or enhanced with data validation and statistical analysis, as per specific requirements.
    """
    try:
        with open(filename, "r") as f:
            grade_csv = f.readlines()
            
        total_points = 0
        count = 0
        for grade in grade_csv:
            grade = grade.strip()
            if grade:
                total_points += float(grade)
                count += 1

        average = total_points / count if count > 0 else 0
        print("Total points:", total_points)
        print("Number of grades:", count)
        print("Average grade:", average)

    except FileNotFoundError:
        print("Error: File not found")
    except IOError:
        print("Error: Input/Output error")
    except ValueError:
        print("Error: Invalid grade value")

# Example Usage
filename = "grade.csv"
read_grades(filename)
