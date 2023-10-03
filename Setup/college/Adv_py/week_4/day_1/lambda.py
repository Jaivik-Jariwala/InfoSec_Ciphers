from functools import reduce

# Define a function to calculate the cube of a number
def cube(y):
    return y * y * y

# Define a lambda function to calculate the cube of a number
lambda_cube = lambda y: y * y * y

# Print the cube of 5 using the function defined with 'def'
print("Using function defined with def:", cube(5))

# Print the cube of 5 using the lambda function
print("Using the lambda function, cube:", lambda_cube(5))

# List of numbers
num = [1, 2, 3, 4, 5]

# Use the 'map' function to double each element in the 'num' list
mapped_result = list(map(lambda x: x * 2, num))
print("Map result:", mapped_result)

# Use the 'filter' function to retain only the even elements from the 'num' list
filtered_res = list(filter(lambda x: x % 2 == 0, num))
print("Filtered:", filtered_res)

# Use the 'reduce' function to find the sum of all elements in the 'num' list
reduced_res = reduce(lambda x, y: x + y, num)
print("Reduced result:", reduced_res)
