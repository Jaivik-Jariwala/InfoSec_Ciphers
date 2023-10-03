'''import os 
def read_csv(filename):
    try:
        with open(filename,"filename.csv"):
            data = filename.readlines()
        sum = 0
        count = 0
        for line in data:
            number = float(line.strip())
            sum += number
            count += 1      
        if count >0 :
            average = sum/count
        else:
            print("error, file is empty")
    
    
    except FileNotFoundError:
        print("file not found")
    except IOError:
        print("io error")
    except ValueError:
        print("invalid values")
''' 
import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

def calculate_avg(data):
    total_sum = 0
    count = 0
    for line in data:
        try:
            number = float(line[0])
            total_sum += number
            count += 1
        except ValueError:
            print(f"Error: Invalid value '{line[0]}' in the file")

    if count > 0:
        average = total_sum / count
        print(f"Average of {count} numbers: {average:.2f}")
    else:
        print("Error: No valid numbers found in the file")

# Example usage
filename = "data.csv"  # Replace with the name of your CSV file
data = read_csv(filename)
calculate_avg(data)
