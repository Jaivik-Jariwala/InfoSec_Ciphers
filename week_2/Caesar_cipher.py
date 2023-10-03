'''
Caesar Cipher 
1. simple encryption Technique used by Julius Caesar to send message
2. works by shifting the letters in plaintext message by certain positions, known as shift and key 

Encryption Phase 
with shift n  :
En(x) = (x+n)mod 26

Decryption Phase 
with shift n  :
Dn(x) = (x-n)mod 26

Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift: 23
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

features of CC
1. Substitution Cipher
2. Fixed Key
3. Symmetric Encryption
4. Limited Keyspace
5. Vulnerable to brute Force
6. Easy to implement 

Algorithm 
1. choose shift value between 1 and 25
2. write down the alphabet in order from A to Z
3. Create new alphabet by shifting each letter of og alpha by shift value
4. A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
5. Replace each letter of message with corresponding letter from new alpha
6. decrypt the message, shift each letter back by the same amt
'''

def encrypt(text,s):
    res = ""

    #traversal
    for i in range(len(text)):
        char = text[i]

        #encrypt uppercase char
        if (char.isupper()):
            res += char((ord(char) + s - 65) % 26 + 65)
        
        #encrypt lowercase char
        else:
            res += char((ord(char) + s - 97) % 26 + 97)
    
    return res

#test case
text = "Hi, I'm Jaivik"
s=16
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher : " + encrypt(text,s))