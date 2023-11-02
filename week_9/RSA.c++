#include <iostream>
#include <cmath>
#include <random>

using namespace std;

// Function to compute the greatest common divisor (GCD)
int gcd(int a, int h) {
    int temp;
    while (1) {
        temp = a % h;
        if (temp == 0)
            return h;
        a = h;
        h = temp;
    }
}

int main() {
    // Two random prime numbers
    double p = random(2,1000);
    double q = random(2,1000);

    // First part of public key: n
    double n = p * q;

    // Finding the other part of the public key (e stands for encrypt)
    double e =random(1, 12);;
    double phi = (p - 1) * (q - 1);

    while (e < phi) {
        // e must be co-prime to phi and smaller than phi.
        if (gcd(e, phi) == 1)
            break;
        else
            e++;
    }

    // Private key (d stands for decrypt), choosing d such that it satisfies d*e = 1 + k * totient
    int k = 2; // A constant value
    double d = (1 + (k * phi)) / e;

    // Message to be encrypted
    double msg = 12;

    cout << "Message data = " << msg << endl;

    // Encryption c = (msg ^ e) % n
    double c = pow(msg, e);
    c = fmod(c, n);
    cout << "Encrypted data = " << c << endl;

    // Decryption m = (c ^ d) % n
    double m = pow(c, d);
    m = fmod(m, n);
    cout << "Original Message Sent = " << m << endl;

    return 0;
}
