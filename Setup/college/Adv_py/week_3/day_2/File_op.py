import os
import shutil
import time
import random

def main():
    file_nam = "file_op.txt"

#writing operation in file
    write_to_file(file_nam)
    print("_______")

#reading operation from file
    read_from_file(file_nam)
    print("_______")

#reading single line from file
    read_single_line(file_nam)
    print("_______")

#reading all line from a file
    read_all_lines(file_nam)
    print("_______")

#writing list in files
    write_list_to_files(file_nam)
    print("_______")

#using pointer to point specific line in files
    move_file_pointer(file_nam)
    print("_______")

#flushing the file buffer
    flush_file_buffer(file_nam)
    print("________")

# closing the file explicitly
    close_file_explicitly(file_nam)
    print("________")

#renaming the files 
    new_file_name = "renames.txt"
    rename_file("to_rename.txt",new_file_name)
    print("_________")


    get_change_file_permission(file_nam)
    print("__________")

#getting metadata
    get_file_metadata(file_nam)
    print("__________")

def write_to_file(file_nam):
    with open(file_nam, "w") as file:
        data_to_write = " this is sample "
        file.write(data_to_write)

def read_from_file(file_nam):
    with open(file_nam, "r") as file:
        content = file.read()
        print("reading the file ")
        print(content)

def read_single_line(file_nam):
    with open(file_nam, "r") as file:
        lines = file.readline()
        print("reading all lines")
        print(lines)

def read_all_lines(file_nam):
    with open(file_nam, "r") as file:
        lines = file.readlines()
        print("reading all lines")
        print(lines)

def write_list_to_files(file_nam):
    line_to_write = ["this is another line"]
    with open(file_nam, "a") as file:
        file.writelines(line_to_write)

def move_file_pointer(file_nam):
    with open(file_nam, "r") as file:
        print("current position of the file pointer:", file.tell())
        file.seek(15)
        print("move file pointer to position 15 ")
        print("current position of the file pointer:", file.tell())
        content = file.read()
        print("reading the file after seek")
        print(content)

def flush_file_buffer(file_name):
    with open(file_name, "r") as file:
        print("\nReading data before flush()")
        print(file.read())
        file.flush()  # Flush the internal buffer of the file
        print("Reading data after flush()")
        print(file.read())  # As the buffer is flushed, no content will be displayed
        print("File buffer flushed")

def close_file_explicitly(file_nam):
    file = open(file_nam, "r")
    print("the file is open")
    file.close()
    print("file is closed explicitly")

def rename_file(old_file_name, new_file_name):
    try:
        os.rename(old_file_name, new_file_name)
        print("file", old_file_name, "renamed to", new_file_name)
    except FileNotFoundError:
        print("file,", old_file_name, "does not exist")
    except FileExistsError:
        print("a file with name", new_file_name, "already exists")

def get_change_file_permission(file_nam):
    file_permissions = os.stat(file_nam).st_mode
    print("file permission in octal:", oct(file_permissions))
    os.chmod(file_nam, stat.S_IRWXG)

def get_file_metadata(file_nam):
    file_stat = os.stat(file_nam)
    print("file size:", file_stat.st_size, "bytes")
    print("file name:", os.path.basename(file_nam))
    print("file type:", "directory" if os.path.isdir(file_nam) else "file")
    print("creation time:", time.ctime(file_stat.st_ctime))
    print("last access time:", time.ctime(file_stat.st_atime))
    print("last modification time:", time.ctime(file_stat.st_mtime))
    print("disk usage info:", shutil.disk_usage("C:/"))

if __name__ == "__main__":
    main()