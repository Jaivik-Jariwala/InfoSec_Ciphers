# RSA Signatures

The **RSA** public-key cryptosystem provides a **digital signature scheme** (sign + verify), based on the math of the **modular exponentiations** and discrete logarithms and the computational difficulty of [**the RSA problem**](https://en.wikipedia.org/wiki/RSA_problem) (and its related integer factorization problem). The [**RSA sign / verify**](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Signing_messages) algorithm works as described below.

## Key Generation[](https://cryptobook.nakov.com/digital-signatures/rsa-signatures#key-generation)

The RSA algorithm uses **keys** of size 1024, 2048, 4096, ..., 16384 bits. RSA supports also longer keys (e.g. 65536 bits), but the performance is too slow for practical use (some operations may take several minutes or even hours). For 128-bit security level, a 3072-bit key is required.

The **RSA key-pair** consists of:

* public key { ***n*** ,  ***e*** }
* private key { ***n*** ,  ***d*** }

The numbers ***n*** and ***d*** are typically big integers (e.g. 3072 bits), while ***e*** is small, typically 65537.

By definition, the RSA key-pairs has the following property:

(��)�≡(��)�≡�(mod�)**(**m**e**)**d**≡**(**m**d**)**e**≡**m**(**mod**n**)**

 for all ***m*** in the range [0... ***n*** )

## RSA Sign[](https://cryptobook.nakov.com/digital-signatures/rsa-signatures#rsa-sign)

**Signing** a message ***msg*** with the private key exponent  ***d*** :

* **1.**Calculate the message hash: ***h*** = hash( ***msg*** )
* **2.**Encrypt ***h*** to calculate the signature: �=ℎ�(mod�)**s**=**h**d**(**mod**n**)

The hash ***h*** should be in the range [0... ***n*** ). The obtained **signature*****s*** is an integer in the range [0... ***n*** ).

## RSA Verify Signature[](https://cryptobook.nakov.com/digital-signatures/rsa-signatures#rsa-verify-signature)

**Verifying** a signature ***s*** for the message ***msg*** with the public key exponent  ***e*** :

* **1.**Calculate the message hash: ***h*** = hash( ***msg*** )
* **2.**Decrypt the signature: ℎ′=��(mod�)**h**′**=**s**e**(**mod**n**)**
* **3.**Compare ***h*** with ***h'*** to find whether the signature is valid or not

If the signature is correct, then the following will be true:

ℎ′=��(mod�)=(ℎ�)�(mod�)=ℎ**h**′**=**s**e**(**mod**n**)**=**(**h**d**)**e**(**mod**n**)**=**h**


The **RSA sign / verify algorithm** is pretty simple. Let's implement it with some code.
