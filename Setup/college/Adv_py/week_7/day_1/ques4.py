class FileNotFoundError(Exception):
    """Custom exception for file not found errors."""
    pass

class InvalidInputDataError(Exception):
    """Custom exception for invalid input data errors."""
    pass

class DiskSpaceFullError(Exception):
    """Custom exception for disk space full errors."""
    pass

def read_input_data(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read and process the input data here
            data = file.read()
            # Example: Check for unexpected data
            if not isinstance(data, str):
                raise InvalidInputDataError("Invalid input data: Expected text but found non-string data.")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: '{file_path}'")
    except OSError as e:
        # Handle disk space full error
        if "No space left on device" in str(e):
            raise DiskSpaceFullError("Disk space is full. Cannot write output file.")
        else:
            raise

def process_data(input_data):
    try:
        # Perform text processing operations here
        # Example: Count words, calculate character frequencies, generate word clouds
        pass
    except Exception as e:
        raise InvalidInputDataError(f"Invalid input data: {str(e)}")

def write_output_data(output_data, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            # Write the processed data to the output file here
            file.write(output_data)
    except OSError as e:
        # Handle disk space full error when writing the output file
        if "No space left on device" in str(e):
            raise DiskSpaceFullError("Disk space is full. Cannot write output file.")
        else:
            raise

# Example usage of the above functions:
try:
    input_file_path = input("Enter the input file path: ")
    output_file_path = input("Enter the output file path: ")

    input_data = read_input_data(input_file_path)
    processed_data = process_data(input_data)
    write_output_data(processed_data, output_file_path)

    print("Text processing completed successfully.")
except FileNotFoundError as e:
    print(f"Error: {str(e)}")
except InvalidInputDataError as e:
    print(f"Error: {str(e)}")
except DiskSpaceFullError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
