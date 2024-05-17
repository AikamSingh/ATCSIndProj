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
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    d = pow(e, -1, phi_n)
    
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

def rsa_encrypt_text(public_key, plaintext):
    """Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - all({0 < ord(c) < public_key[0] for c in plaintext})
    """
    n, e = public_key
    encrypted = []
    for letter in plaintext:
        encrypted.append(str((ord(letter) ** e) % n))
    
    # Join the encrypted numbers with a space for easy separation
    return ' '.join(encrypted)

def rsa_decrypt_text(private_key, ciphertext):
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - all({0 < ord(c) < private_key[0] * private_key[1] for c in ciphertext})
    """
    p, q, d = private_key
    n = p * q

    decrypted = []
    for encrypted_letter in ciphertext.split():
        decrypted.append(chr((int(encrypted_letter) ** d) % n))
    
    return ''.join(decrypted)




def main():
    # Generate RSA keys using two prime numbers
    p = 7
    q = 11
    private_key, public_key = generate_key(p, q)
    
    print(f"Private key: {private_key}")
    print(f"Public key: {public_key}")
    
    # Encrypt a plaintext number (e.g., 5)
    plaintext_number = 5
    encrypted_number = rsa_encrypt(public_key, plaintext_number)
    print(f"Encrypted number: {encrypted_number}")
    
    # Decrypt the ciphertext number
    decrypted_number = rsa_decrypt(private_key, encrypted_number)
    print(f"Decrypted number: {decrypted_number}")
    
    # Check if decryption is correct
    if decrypted_number == plaintext_number:
        print("Number encryption and decryption successful!")
    else:
        print("Number encryption and decryption failed!")
    
    # Encrypt a plaintext text (e.g., "HELLO")
    plaintext_text = "HELLO"
    encrypted_text = rsa_encrypt_text(public_key, plaintext_text)
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the ciphertext text
    decrypted_text = rsa_decrypt_text(private_key, encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
    
    # Check if decryption is correct
    if decrypted_text == plaintext_text:
        print("Text encryption and decryption successful!")
    else:
        print("Text encryption and decryption failed!")

if __name__ == "__main__":
    main()
