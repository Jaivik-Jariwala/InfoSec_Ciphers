import base64
import zlib

class DataProcessor:
    def __init__(self):
        self.storage = []
    
    def encode(self, text):
        encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return encoded_text
    
    def decode(self, encoded_text):
        decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
        return decoded_text
    
    def buffer(self, data):
        self.storage.append(data)
    
    def compress(self, data):
        compressed_data = zlib.compress(data.encode('utf-8'))
        return compressed_data
    
    def decompress(self, compressed_data):
        decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
        return decompressed_data
    
    def process(self, data):
        encoded_data = self.encode(data)
        self.buffer(encoded_data)
        compressed_data = self.compress(encoded_data)
        decompressed_data = self.decompress(compressed_data)
        decoded_data = self.decode(decompressed_data)
        return decoded_data

def main():
    data = "This is a sample text for demonstration purposes."
    
    processor = DataProcessor()
    processed_data = processor.process(data)
    
    print("Original Data:", data)
    print("Processed Data:", processed_data)

if __name__ == "__main__":
    main()
