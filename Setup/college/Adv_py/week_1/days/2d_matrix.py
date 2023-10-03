# Function to create a 2D array (matrix) without built-in functions
def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            # For simplicity, we'll use row index + column index as the value for each element
            # You can replace this with your desired values
            element = i + j
            row.append(element)
        matrix.append(row)
    return matrix

# Example usage
rows = 3
columns = 4
matrix = create_matrix(rows, columns)

# Print the matrix
for row in matrix:
    print(row)
