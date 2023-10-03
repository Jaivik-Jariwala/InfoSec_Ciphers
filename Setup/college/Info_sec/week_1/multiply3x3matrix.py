def matrix_multiplication(A, B):
    """
    Perform matrix multiplication of two given matrices.

    Args:
        A (list of lists): The first matrix.
        B (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix after matrix multiplication.
    """

    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are incompatible for multiplication.")

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Initialize a matrix to store the result of multiplication
    multiply = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for n in range(rows_A):
        for m in range(cols_B):
            for o in range(rows_B):
                multiply[n][m] += A[n][o] * B[o][m]

    return multiply

# Test the matrix multiplication
A = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]
B = [[3, 4, 5], [3, 4, 5], [3, 4, 5]]

try:
    result = matrix_multiplication(A, B)
    print("The multiplication result is:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
