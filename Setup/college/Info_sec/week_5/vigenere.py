class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _extend_key(self, length):
        extended_key = self.key
        while len(extended_key) < length:
            extended_key += self.key
        return extended_key[:length]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        extended_key = self._extend_key(len(plaintext))
        ciphertext = ''
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += encrypted_char
            else:
                ciphertext += plaintext[i]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        extended_key = self._extend_key(len(ciphertext))
        plaintext = ''
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
                plaintext += decrypted_char
            else:
                plaintext += ciphertext[i]
        return plaintext


def main():
    key = input("Enter the encryption key: ")
    vigenere = VigenereCipher(key)

    plaintext = input("Enter the plaintext: ")
    encrypted_message = vigenere.encrypt(plaintext)
    print("Encrypted Message:", encrypted_message)



if __name__ == "__main__":
    main()
