#include <iostream>
#include <string>
#include <fstream>
#include <cryptopp/cryptlib.h>
#include <cryptopp/rsa.h>
#include <cryptopp/sha.h>
#include <cryptopp/files.h>
#include <cryptopp/hex.h>

using namespace CryptoPP;

int main() {
    AutoSeededRandomPool rng;

    // Generate an RSA key pair
    InvertibleRSAFunction params;
    params.GenerateRandomWithKeySize(rng, 2048);

    RSA::PrivateKey privateKey(params);
    RSA::PublicKey publicKey(params);

    // Load the file to be signed
    std::string filename = "example.txt";
    std::string fileContents;
    std::ifstream inputFile(filename, std::ios::binary);

    if (!inputFile) {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    inputFile.seekg(0, std::ios::end);
    fileContents.resize(inputFile.tellg());
    inputFile.seekg(0, std::ios::beg);
    inputFile.read(&fileContents[0], fileContents.size());

    inputFile.close();

    // Compute the SHA-256 hash of the file
    SHA256 sha256;
    byte hash[SHA256::DIGESTSIZE];
    sha256.CalculateDigest(hash, (const byte*)fileContents.data(), fileContents.size());

    // Sign the hash with the private key to create the digital signature
    RSASSA_PKCS1v15_SHA_Signer signer(privateKey);
    size_t signatureLength = signer.MaxSignatureLength();
    std::string signature(signatureLength, 0x00);

    signer.SignMessage(rng, (const byte*)hash, SHA256::DIGESTSIZE, (byte*)signature.data());

    // Save the digital signature to a file
    FileSink signatureFile("signature.sig");
    signatureFile.Put((const byte*)signature.data(), signatureLength);

    // Verify the digital signature with the public key
    RSASSA_PKCS1v15_SHA_Verifier verifier(publicKey);

    bool signatureVerified = false;
    FileSource("signature.sig", true, new SignatureVerificationFilter(verifier, nullptr,
        SignatureVerificationFilter::THROW_EXCEPTION
    ));

    if (signatureVerified) {
        std::cout << "Signature verified successfully. The file is authentic." << std::endl;
    } else {
        std::cerr << "Signature verification failed. The file may be tampered." << std::endl;
    }

    return 0;
}
