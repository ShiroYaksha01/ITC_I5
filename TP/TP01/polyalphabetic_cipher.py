"""Vigenere polyalphabetic cipher, implemented without encryption libraries.

Input: nonempty English letters only (A-Z, case-insensitive).
Output: uppercase letters. A short key is repeated to cover the message.
"""


def validate_letters(text):
    if not text or any(char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                       for char in text):
        raise ValueError("Use nonempty English letters only (A-Z), without spaces.")
    return text.upper()


def encrypt(plaintext, key):
    plaintext = validate_letters(plaintext)
    key = validate_letters(key)
    ciphertext = ""

    for i in range(len(plaintext)):
        # A = 0, B = 1, ..., Z = 25. Modulo repeats a short key.
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = validate_letters(ciphertext)
    key = validate_letters(key)
    plaintext = ""

    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))

    return plaintext


def main():
    # Change these values to try your own plaintext and provided keys.
    plaintext = "HELLO"
    cases = [("Case 1: key equals plaintext length", "XMCKL"),
             ("Case 2: key is shorter than plaintext", "KEY")]

    print("POLYALPHABETIC CIPHER (VIGENERE)")
    for title, key in cases:
        print("\n" + title)
        print("Plaintext:", plaintext, "| Length:", len(plaintext))
        print("Provided key:", key, "| Length:", len(key))
        effective_key = "".join(key[i % len(key)] for i in range(len(plaintext)))
        print("Effective key:", effective_key)
        ciphertext = encrypt(plaintext, key)
        recovered = decrypt(ciphertext, key)
        print("Ciphertext:", ciphertext)
        print("Decrypted plaintext:", recovered)
        print("Recovered original:", recovered == plaintext.upper())


if __name__ == "__main__":
    main()
