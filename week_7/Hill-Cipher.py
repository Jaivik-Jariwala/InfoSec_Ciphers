def matrix_multiply(matrix1, matrix2, mod):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= mod
    return result

def matrix_inverse(matrix, mod):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det %= mod
    det_inverse = None

    for i in range(1, mod):
        if (det * i) % mod == 1:
            det_inverse = i
            break

    if det_inverse is None:
        return None

    adjugate = [
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ]

    inverse = [
        [0, 0],
        [0, 0]
    ]

    for i in range(2):
        for j in range(2):
            inverse[i][j] = (adjugate[i][j] * det_inverse) % mod

    return inverse

def ngram_encrypt(plain_text, key_matrix, n, mod):
    if len(plain_text) % n != 0:
        raise ValueError("Plain text length must be a multiple of the n-gram size.")

    ngrams = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    encrypted_ngrams = []

    for ngram in ngrams:
        ngram = [ord(c) - ord('A') for c in ngram]
        encrypted_ngram = matrix_multiply([ngram], key_matrix, mod)
        encrypted_ngrams.append(encrypted_ngram[0])

    encrypted_text = ''
    for ngram in encrypted_ngrams:
        encrypted_text += ''.join([chr(x + ord('A')) for x in ngram])

    return encrypted_text

def ngram_decrypt(encrypted_text, key_matrix, n, mod):
    if len(encrypted_text) % n != 0:
        raise ValueError("Encrypted text length must be a multiple of the n-gram size.")

    ngrams = [encrypted_text[i:i + n] for i in range(0, len(encrypted_text), n)]
    key_inverse = matrix_inverse(key_matrix, mod)

    if key_inverse is None:
        raise ValueError("Key matrix is not invertible.")

    decrypted_ngrams = []

    for ngram in ngrams:
        ngram = [ord(c) - ord('A') for c in ngram]
        decrypted_ngram = matrix_multiply([ngram], key_inverse, mod)
        decrypted_ngrams.append(decrypted_ngram[0])

    decrypted_text = ''
    for ngram in decrypted_ngrams:
        decrypted_text += ''.join([chr(x + ord('A')) for x in ngram])

    return decrypted_text

def main():
    key_matrix = [
        [3, 2],
        [5, 7]
    ]
    n = 3
    mod = 26
    plain_text = "JaivikRaj"

    encrypted_text = ngram_encrypt(plain_text, key_matrix, n, mod)
    print("Encrypted text:", encrypted_text)

    decrypted_text = ngram_decrypt(encrypted_text, key_matrix, n, mod)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
