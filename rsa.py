#!/usr/bin/env python3


"""
rsa.py
This is a template for a Python program
"""

__author__ = "Aikam Singh"
__version__ = "2024-05-10"

import math
import random


def generate_key(p, q):
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (p, q, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - p and q are prime
        - p != q
    """
    # Compute the product of p and q
    n = p * q
    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)
    # Since e is chosen randomly, we repeat the random choice
    # until e is coprime to phi_n.
    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # Choose d such that e * d % phi_n = 1.
    # Notice that we're using our modular_inverse from our work in the last chapter!
    d = (1 + (k*phi))/e
    return ((p, q, d), (n, e))

def rsa_encrypt(public_key, plaintext):
    """Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - 0 < plaintext < public_key[0]
    """
    n, e = public_key[0], public_key[1]

    encrypted = (plaintext ** e) % n

    return encrypted

def rsa_decrypt(private_key, ciphertext):
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - 0 < ciphertext < private_key[0] * private_key[1]
    """
    p, q, d = private_key[0], private_key[1], private_key[2]
    n = p * q

    decrypted = (ciphertext ** d) % n

    return decrypted

def main():
    #the program goes here
    generate_key(7, 11)

if __name__ == "__main__":
    main()