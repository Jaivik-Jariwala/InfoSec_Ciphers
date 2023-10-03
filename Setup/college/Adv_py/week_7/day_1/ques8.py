import os
import subprocess

# Define file extensions and their corresponding subfolders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".ppt", ".xlsx", ".csv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"]
}

# Create subfolders in the sorted_files directory
sorted_dir = "sorted_files"
for folder in file_types.keys():
    folder_path = os.path.join(sorted_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to organize files
def organize_files(src_folder, dest_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[-1].lower()

            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination = os.path.join(dest_folder, category, file)
                    subprocess.run(["mv", file_path, destination], check=True)
                    break

# Organize files in the "unsorted_files" folder
unsorted_folder = "unsorted_files"
organize_files(unsorted_folder, sorted_dir)

# Generate a report
def generate_report():
    report = {}
    for category in file_types.keys():
        category_folder = os.path.join(sorted_dir, category)
        count = len(os.listdir(category_folder))
        report[category] = count
    return report

report_data = generate_report()
print("Files organized into categories:")
for category, count in report_data.items():
    print(f"{category}: {count} files")
