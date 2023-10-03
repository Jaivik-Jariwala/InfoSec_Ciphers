def rail_fence_encrypt(message, rails):
    fence = [[' ' for _ in range(len(message))] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in message:
        fence[rail][fence[rail].index(' ')] = char
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    ciphertext = ''
    for rail in fence:
        ciphertext += ''.join(rail)
    
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    fence = [[' ' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    index = 0
    for rail in fence:
        for i in range(len(rail)):
            if rail[i] == '*':
                rail[i] = ciphertext[index]
                index += 1
    
    plaintext = ''
    rail = 0
    direction = 1
    
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][0]
        fence[rail][0] = ' '
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    return plaintext

def main():
    print("Rail Fence Cipher")
    message = input("Enter the message: ")
    rails = int(input("Enter the number of rails: "))
    
    encrypted_message = rail_fence_encrypt(message, rails)
    decrypted_message = rail_fence_decrypt(encrypted_message, rails)
    
    print("\nEncrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
