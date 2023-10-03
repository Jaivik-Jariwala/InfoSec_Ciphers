import zlib

# Create sample data 
data = "this is sample data to be compressed." * 1000

# Convert the data 
data_bytes = data.encode('utf-8')

#applying the data compression and decompression method 

# Compress the data using zlib
compressed_data = zlib.compress(data_bytes)

# Decompress the compressed data
decompressed_data = zlib.decompress(compressed_data)

# Convert the decompressed bytes back to a string
original_data = decompressed_data.decode('utf-8')


# Print the length of original and compressed data
print("Original data length:", len(data))
print("Compressed data length:", len(compressed_data))

# Print the first few characters of the original data
print("Original data:", data[:50])

# Print the first few characters of the decompressed data
print("Decompressed data:", original_data[:50])
