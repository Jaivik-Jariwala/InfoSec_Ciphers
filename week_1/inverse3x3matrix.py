def determinant_2x2(matrix):
    """
    Calculate the determinant of a 2x2 matrix.

    Args:
        matrix (list of lists): The 2x2 matrix for which the determinant is to be calculated.

    Returns:
        int or float: The determinant of the 2x2 matrix.
    """

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    """
    Calculate the determinant of a 3x3 matrix.

    Args:
        matrix (list of lists): The 3x3 matrix for which the determinant is to be calculated.

    Returns:
        int or float: The determinant of the 3x3 matrix.
    """

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * determinant_2x2([[e, f], [h, i]]) - b * determinant_2x2([[d, f], [g, i]]) + c * determinant_2x2([[d, e], [g, h]])

def transpose(matrix):
    """
    Transpose a given matrix.

    Args:
        matrix (list of lists): The matrix to be transposed.

    Returns:
        list of lists: The transposed matrix.
    """

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def cofactor_matrix(matrix):
    """
    Calculate the cofactor matrix of a given matrix.

    Args:
        matrix (list of lists): The matrix for which the cofactor matrix is to be calculated.

    Returns:
        list of lists: The cofactor matrix of the input matrix.
    """

    cofactors = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix[0])):
            minor_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * determinant_2x2(minor_matrix))
        cofactors.append(cofactor_row)
    return cofactors

def scalar_multiply(matrix, scalar):
    """
    Multiply a given matrix by a scalar.

    Args:
        matrix (list of lists): The matrix to be multiplied.
        scalar (int or float): The scalar value to multiply the matrix by.

    Returns:
        list of lists: The resulting matrix after scalar multiplication.
    """

    return [[scalar * element for element in row] for row in matrix]

def inverse_3x3(matrix):
    """
    Calculate the inverse of a 3x3 matrix.

    Args:
        matrix (list of lists): The 3x3 matrix for which the inverse is to be calculated.

    Returns:
        list of lists: The inverse of the 3x3 matrix.

    Raises:
        ValueError: If the matrix is singular, i.e., its determinant is zero and its inverse does not exist.
    """

    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("The matrix is singular, and its inverse does not exist.")
    
    cofactors = cofactor_matrix(matrix)
    adjugate = transpose(cofactors)
    inverse = scalar_multiply(adjugate, 1/det)
    
    return inverse

# Test the inverse function
matrix = [[1, 1, 3], [4, 5, 4], [9, 14, 13]]
try:
    inv_matrix = inverse_3x3(matrix)
    print("Inverse of the matrix:")
    for row in inv_matrix:
        print(row)
except ValueError as e:
    print(e)
