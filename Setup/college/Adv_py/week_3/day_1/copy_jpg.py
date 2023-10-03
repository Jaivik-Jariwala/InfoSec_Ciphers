'''
import os
import shutil

def copy_jpg_files(source_folder):
    # Get the list of files in the source folder
    files = os.listdir(source_folder)
    
    # Filter JPG files
    jpg_files = [file for file in files if file.lower().endswith('.jpg')]
    
    # Copy JPG files to the working directory
    for jpg_file in jpg_files:
        source_path = os.path.join(source_folder, jpg_file)
        destination_path = os.path.join(os.getcwd(), jpg_file)
        shutil.copy(source_path, destination_path)
        print(f"Copied {jpg_file} to working directory")

# Specify the source folder
source_folder = '/path/to/source/folder'

# Call the function to copy JPG files
copy_jpg_files(source_folder)
'''

import os
import shutil 
dest_directory = 'destination'
os.makedirs(dest_directory)
print("new directory created :", dest_directory)
source_directory = "source"
for filename in os.listdir(source_directory):
    if filename.endswith(".jpg"):
        source_file = os.path(source_directory, filename)
        destination_file = os.path.join(dest_directory,filename)
        shutil.copy(source_directory,dest_directory)
        print("copied ",source_file "_>" , destination_file)
current_directory = os.getcwd()