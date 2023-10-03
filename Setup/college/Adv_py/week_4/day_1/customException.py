# Define custom exception class
class InvalidHumanException(Exception):
    "Raised when the input color is black"
    pass

# Input color from the user
color = input("Enter color: ")

# Define the checkHumanity function with proper parentheses
def checkHumanity():
    # Check if the color is black and raise the custom exception
    if color.lower() == "black":
        raise InvalidHumanException
    else:
        print("Eligible human")

try:
    # Try to catch the custom exception and handle it
    checkHumanity()
except InvalidHumanException:
    print("Invalid human Occurred: Invalid Human")
