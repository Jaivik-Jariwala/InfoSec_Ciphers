# When reading from or writing to files, encoding should be specified to handle text in the desired character set.

# Writing to a file with specified encoding
with open("encoded_file.txt", "w", encoding="uf-8") as file:
    file.write("Hello, 你好, مرحبًا")

# Encoding ensures that the file can handle and correctly represent characters from different languages,
# like the English, Chinese, and Arabic characters in the provided string.
# Reading from the file with specified encoding
with open("encoded_file.txt", "r", encoding=utf-8) as file:
    content = file.read()
    print(f"file content : {content}")
print("file encoding done")

