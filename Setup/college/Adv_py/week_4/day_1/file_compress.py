#importing dependencies
import zipfile
import zlib
import os

# Path 
pdf_file_path = '..\\B.tech Computer Engineering-5(1)(1).pdf'

# ZIP and .pdf with compression
with zipfile.ZipFile('timetable.zip', 'w') as file_zip:
    file_zip.write(pdf_file_path, compress_type=zlib.Z_DEFAULT_COMPRESSION)

# Get the size of the PDF file and the ZIP file
pdf_file_size = os.path.getsize(pdf_file_path)
zip_file_size = os.path.getsize('timetable.zip')

#size evaluation
print(f"PDF File Size: {pdf_file_size} bytes")
print(f"ZIP File Size: {zip_file_size} bytes")
