def prepare_key(key):
    key = key.upper().replace("J", "I")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for char in key_set:
        alphabet = alphabet.replace(char, "")

    key_matrix = key + alphabet
    return key_matrix

def encrypt(plaintext, key):
    key_matrix = prepare_key(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    n = len(plaintext)

    if n % 2 != 0:
        plaintext += 'X'
        n += 1

    # create the pairs of letters
    pairs = [plaintext[i:i + 2] for i in range(0, n, 2)]

    ciphertext = ""

    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = divmod(key_matrix.index(char1), 5)
        row2, col2 = divmod(key_matrix.index(char2), 5)

        if row1 == row2:
            ciphertext += key_matrix[row1 * 5 + (col1 + 1) % 5]
            ciphertext += key_matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += key_matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += key_matrix[row1 * 5 + col2]
            ciphertext += key_matrix[row2 * 5 + col1]

    return ciphertext

def decrypt(ciphertext, key):
    key_matrix = prepare_key(key)
    ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
    n = len(ciphertext)

    # Pad the ciphertext with 'X' if it has an odd length
    if n % 2 != 0:
        ciphertext += 'X'
        n += 1

    # create the pairs of letters
    pairs = [ciphertext[i:i + 2] for i in range(0, n, 2)]

    plaintext = ""

    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = divmod(key_matrix.index(char1), 5)
        row2, col2 = divmod(key_matrix.index(char2), 5)

        if row1 == row2:
            plaintext += key_matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += key_matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += key_matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += key_matrix[row1 * 5 + col2]
            plaintext += key_matrix[row2 * 5 + col1]

    return plaintext

# Test function
plaintext = "WORKS SECURELY"
key = "CIPHERWORKS"

encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
