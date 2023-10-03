class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)  
print(p1 + p2) 

if p1 == p2:
    print("Points are equal")
else:
    print("Points are not equal")

'''Point Class
The Point class represents a 2D point in a Cartesian coordinate system. It allows for the creation of points, addition of points, and comparison of points.

Class Methods
__init__(self, x, y): Initializes a new Point object with the given x and y coordinates.
__str__(self): Returns a string representation of the Point object in the format "Point(x, y)".
__add__(self, other): Overloads the addition operator to enable adding two Point objects element-wise.
__eq__(self, other): Overloads the equality operator to check if two Point objects have the same coordinates.
'''