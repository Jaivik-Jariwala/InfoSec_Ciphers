import random
import hashlib

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to create a cryptographic hash of a message
def hash_message(message):
    sha256 = hashlib.sha256()
    sha256.update(str(message).encode())
    return int(sha256.hexdigest(), 16)

# Generate two random prime numbers (p and q)
while True:
    p = random.randint(100, 200)
    if is_prime(p):
        break

while True:
    q = random.randint(200, 300)
    if is_prime(q):
        break

n = p * q
phi = (p - 1) * (q - 1)

# Find an encryption key (e) such that 1 < e < phi and gcd(e, phi) = 1
while True:
    e = random.randint(2, phi - 1)
    if gcd(e, phi) == 1:
        break

# Calculate the decryption key (d) using the modular multiplicative inverse of e
d = mod_inverse(e, phi)

# Message to be signed
message = 485

# Hash the message
hashed_message = hash_message(message)

# Sign the hashed message
signature = pow(hashed_message, d, n)

# Verify the signature
if pow(signature, e, n) == hashed_message:
    print("Signature verified: The message is authentic.")
else:
    print("Signature verification failed: The message may be caught by darth .")
