# Python will encode the text based on the default text encoding. 
# Additionally, Python will convert line endings (\n) to whatever the platform-specific line ending is, 
# which would corrupt a binary file like an exe or png file.
# 'wb' mode is specifically designed for writing binary data, such as images, audio files, video files,
# and other non-textual data. When you open a file in binary write mode ('wb'), the data is written 
# as-is without any character encoding or interpretation.

binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # Binary representation of "Hello World"

with open('binary_file.bin', 'wb') as file:
    file.write(binary_data)

with open('binary_file.bin', 'rb') as file:
    content = file.read()
    print(f"File Content: {content}")

print("Task3: writing binary file is done")