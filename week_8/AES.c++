#include <iostream>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>

using namespace CryptoPP;

int main() {
    byte key[AES::DEFAULT_KEYLENGTH] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};
    byte iv[AES::BLOCKSIZE] = {0};

    std::string plainText = "This is a secret message.";
    std::string cipherText;
    std::string decryptedText;

    AES::Encryption aesEncryption(key, AES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Encryption cbcEncryption(aesEncryption, iv);

    // Encrypt
    StringSource(plainText, true,
        new StreamTransformationFilter(cbcEncryption, new StringSink(cipherText)));

    // Decrypt
    AES::Decryption aesDecryption(key, AES::DEFAULT_KEYLENGTH);
    CBC_Mode_ExternalCipher::Decryption cbcDecryption(aesDecryption, iv);

    StringSource(cipherText, true,
        new StreamTransformationFilter(cbcDecryption, new StringSink(decryptedText)));

    std::cout << "Original Text: " << plainText << std::endl;
    std::cout << "Encrypted Text: " << cipherText << std::endl;
    std::cout << "Decrypted Text: " << decryptedText << std::endl;

    return 0;
}
