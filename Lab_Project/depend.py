import sys

def depends(plain_text):
    text_size = sys.getsizeof(plain_text)
    k = 3
    m = text_size
    c = 4
    return text_size, k, m, c
