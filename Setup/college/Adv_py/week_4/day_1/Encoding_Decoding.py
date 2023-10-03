#encoding and decoding
# Python uses Unicode for handling text, and the 'encode()' and 'decode()' methods are used to convert text to bytes and vice versa.

txt = "Hello, 你好, مرحبًا"
encoded_txt = txt.encode('utf-8')

#Unicode is a list of characters with unique decimal numbers (code points).  A = 65, B = 66, C = 67, ..
# UTF-8 is a variable-length character encoding standard used for electronic communication.
print(f"encoded text: {encoded_txt}")

decoded_txt = encoded_txt.decode('utf-8')
print(f"decoded text: {decoded_txt}")

print("encoding - decoding done")