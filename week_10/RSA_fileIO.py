from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate an RSA key pair for the sender
sender_key = RSA.generate(2048)

# Generate an AES key for message encryption
aes_key = get_random_bytes(16)  # AES key with 128 bits (16 bytes)

# Encrypt the message with AES
message = "This is a test message.".encode('utf-8')
cipher = AES.new(aes_key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message, AES.block_size))

# Sender signs the ciphertext
private_key = sender_key.export_key()
sender_private_key = RSA.import_key(private_key)
h = SHA.new(ciphertext)
signature = pkcs1_15.new(sender_private_key).sign(h)

# Receiver verifies the sender's signature
public_key = sender_key.publickey().export_key()
sender_public_key = RSA.import_key(public_key)
h = SHA.new(ciphertext)

try:
    pkcs1_15.new(sender_public_key).verify(h, signature)
    print("Sender's signature verified: The message is authentic.")

    # The receiver decrypts the message with the AES key
    cipher = AES.new(aes_key, AES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    print("Decrypted message:", decrypted_message)
except (ValueError, TypeError):
    print("Signature verification failed: The message may be tampered with.")
