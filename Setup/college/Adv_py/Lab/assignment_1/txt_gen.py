import os

# Create a directory for testing
test_directory = "test_reviews"
os.makedirs(test_directory, exist_ok=True)

# Create sample review data
review_data = [
    "Customer ID: ABC123",
    "Product ID: XYZ789",
    "Review Date: 2023-07-15",
    "Review Rating: 4",
    "Review Text: This is a sample review."
]

# Create sample text files with review data
for i in range(1, 6):
    file_name = f"review_{i}.txt"
    file_path = os.path.join(test_directory, file_name)
    
    with open(file_path, "w") as file:
        file.write("\n".join(review_data))

print("Sample directory and files created for testing.")
