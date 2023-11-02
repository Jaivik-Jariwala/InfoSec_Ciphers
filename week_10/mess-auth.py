import random
import math
import hashlib

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

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

# Function to generate a key pair
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi)
        if math.gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)
    
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to generate a random prime number
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to sign a message
def sign_message(private_key, message):
    n, d = private_key
    hashed_message = hash_message(message)
    signature = pow(hashed_message, d, n)
    return signature
def verify_signature(public_key, private_key_receiver, encrypted_value):
    n_receiver, d_receiver = private_key_receiver
    n_sender, e_sender = public_key

    # Decrypt the encrypted value with the sender's public key
    decrypted_signature = pow(encrypted_value, e_sender, n_sender)

    # Calculate the hashed message from the decrypted signature
    hashed_message = hash_message(decrypted_signature)

    # Compare the hashed message with the decrypted signature
    return hashed_message == decrypted_signature



# Generate the key pairs with larger bit lengths for better security.
public_key, private_key = generate_keypair(2048)
public_key_receiver, private_key_receiver = generate_keypair(2048)

# Message to be signed
message = "Wolfing here"

# Sign the message
signature = sign_message(private_key, message)

# Verify the signature
if verify_signature(public_key, private_key_receiver, signature):
    print("Signature is valid.")
else:
    print("Signature is invalid.")
