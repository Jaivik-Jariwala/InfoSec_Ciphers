# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map and lambda to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

# Using filter and lambda to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Using reduce and lambda to get the sum of numbers
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
