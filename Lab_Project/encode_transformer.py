from transformer import transform_text
from depend import depends

def Quad(a, b, c, x):
    return a * x   + b * x + c

def encode_text(plain_text, k, m, c):
    transformed_text = transform_text(plain_text)
    encoded_text = [Quad(k, m, c, x) for x in transformed_text]
    return encoded_text
