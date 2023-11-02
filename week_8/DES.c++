#include <iostream>
#include <cryptopp/des.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>

using namespace CryptoPP;

int main() {
    byte key[DES::DEFAULT_KEYLENGTH] = {0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF};
    byte iv[DES::BLOCKSIZE] = {0};

    std::string plainText = "This is a secret message.";
    std::string cipherText;
    std::string decryptedText;

    DES::Encryption desEncryption(key, DES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Encryption cbcEncryption(desEncryption, iv);

    // Encrypt
    StringSource(plainText, true,
        new StreamTransformationFilter(cbcEncryption, new StringSink(cipherText)));

    // Decrypt
    DES::Decryption desDecryption(key, DES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Decryption cbcDecryption(desDecryption, iv);

    StringSource(cipherText, true,
        new StreamTransformationFilter(cbcDecryption, new StringSink(decryptedText)));

    std::cout << "Original Text: " << plainText << std::endl;
    std::cout << "Encrypted Text: " << cipherText << std::endl;
    std::cout << "Decrypted Text: " << decryptedText << std::endl;

    return 0;
}
