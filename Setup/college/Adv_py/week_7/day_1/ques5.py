import json
import bcrypt

# Function to register a new user
def register_user(username, password):
    try:
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Check if the username already exists
    if username in user_data:
        print("Username already exists. Please choose a different one.")
        return False

    # Hash the user's password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store the user's data in the dictionary
    user_data[username] = {
        "password": hashed_password.decode('utf-8')
    }

    # Save the updated user data to the file
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)
    
    print("Registration successful. You can now log in.")
    return True

# Function to authenticate a user
def login_user(username, password):
    try:
        # Load user data from the file
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        print("No users registered yet. Please sign up.")
        return False

    # Check if the username exists
    if username not in user_data:
        print("Username not found. Please register.")
        return False

    # Compare the hashed password
    stored_password = user_data[username]["password"]
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        print("Login successful. Welcome,", username)
        return True
    else:
        print("Invalid password. Please try again.")
        return False

# Example usage:
while True:
    print("\n1. Sign Up\n2. Log In\n3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login_user(username, password):
            # Perform tasks for the logged-in user here
            pass
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")
