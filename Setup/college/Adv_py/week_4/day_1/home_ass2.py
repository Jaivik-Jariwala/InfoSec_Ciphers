class FileOpenError(Exception):
    "Raised when there's an issue opening the file."
    pass

class FileReadError(Exception):
    "Raised when there's an issue reading from the file."
    pass

class FileWriteError(Exception):
    "Raised when there's an issue writing to the file."
    pass

class BinaryFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
    
    def open_file(self, mode):
        try:
            self.file = open(self.file_path, mode)
        except IOError:
            raise FileOpenError("Error opening the file.")
    
    def read_data(self):
        try:
            data = self.file.read()
            return data
        except Exception:
            raise FileReadError("Error reading from the file.")
    
    def write_data(self, data):
        try:
            self.file.write(data)
        except Exception:
            raise FileWriteError("Error writing to the file.")
    
    def close_file(self):
        if self.file is not None:
            self.file.close()
    
def main():
    file_path = "data.bin"
    
    try:
        manager = BinaryFileManager(file_path)
        manager.open_file("wb")
        
        data_to_write = b"This is binary data."
        manager.write_data(data_to_write)
        
        manager.close_file()
        
        manager.open_file("rb")
        read_data = manager.read_data()
        manager.close_file()
        
        print("Data read from the file:", read_data.decode('utf-8'))
        
    except FileOpenError as open_err:
        print("File Open Error:", open_err)
    except FileReadError as read_err:
        print("File Read Error:", read_err)
    except FileWriteError as write_err:
        print("File Write Error:", write_err)

if __name__ == "__main__":
    main()
