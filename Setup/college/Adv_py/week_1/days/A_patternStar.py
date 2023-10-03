# Define the pattern to print the letter 'A'
def print_A_pattern(height):
    width = 2 * height - 1

    for i in range(1, height + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (width - 2 * i + 1)
        print(spaces + stars)

    for i in range(height // 2):
        stars = '*' * width
        print(stars)

# Set the desired height of the 'A'
height = 6

# Print the letter 'A' pattern
print_A_pattern(height)
