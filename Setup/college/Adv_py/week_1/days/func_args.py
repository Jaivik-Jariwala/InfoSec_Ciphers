# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

# Calling functions with different arguments
rectangle_area = calculate_rectangle_area(5, 10)
print("Area of rectangle:", rectangle_area)

circle_area = calculate_circle_area(3)
print("Area of circle:", circle_area)

# You can also use variables as arguments
length = 7
width = 4
rectangle_area2 = calculate_rectangle_area(length, width)
print("Area of rectangle 2:", rectangle_area2)

radius = 2.5
circle_area2 = calculate_circle_area(radius)
print("Area of circle 2:", circle_area2)
