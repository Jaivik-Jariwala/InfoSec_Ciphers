#include <iostream>
#include <string>
#include <cryptopp/rsa.h>
#include <cryptopp/osrng.h>
#include <cryptopp/base64.h>

using namespace CryptoPP;

int main() {
    AutoSeededRandomPool rng;

    InvertibleRSAFunction params;
    params.GenerateRandomWithKeySize(rng, 2048);
    RSA::PrivateKey privateKey(params);
    RSA::PublicKey publicKey(params);

    std::string plaintext = "Hello, RSA!";
    std::string ciphertext, decryptedtext;

    RSAES_OAEP_SHA_Encryptor encryptor(publicKey);
    RSAES_OAEP_SHA_Decryptor decryptor(privateKey);

    StringSource(plaintext, true,
        new PK_EncryptorFilter(rng, encryptor,
            new StringSink(ciphertext)
        )
    );

    StringSource(ciphertext, true,
        new PK_DecryptorFilter(rng, decryptor,
            new StringSink(decryptedtext)
        )
    );

    std::cout << "Original Text: " << plaintext << std::endl;
    std::cout << "Ciphertext (Base64): " << base64_encode(reinterpret_cast<const unsigned char*>(ciphertext.data()), ciphertext.size()) << std::endl;
    std::cout << "Decrypted Text: " << decryptedtext << std::endl;

    return 0;
}
