"""Alphabetic one-time pad arithmetic, without encryption libraries.

Input: nonempty English letters only (A-Z, case-insensitive).
The key must have exactly the same length as the message in this program.
A real OTP also requires a uniformly random, independent, secret key used
only once. The published key below is ONLY a classroom arithmetic example;
length validation cannot establish randomness, secrecy, or non-reuse.
"""


def validate_letters(text):
    if not text or any(char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                       for char in text):
        raise ValueError("Use nonempty English letters only (A-Z), without spaces.")
    return text.upper()


def encrypt(plaintext, key):
    plaintext = validate_letters(plaintext)
    key = validate_letters(key)
    if len(key) != len(plaintext):
        raise ValueError("OTP key must have the same length as the plaintext.")

    ciphertext = ""
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')  # Each key letter is used once; no repetition.
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = validate_letters(ciphertext)
    key = validate_letters(key)
    if len(key) != len(ciphertext):
        raise ValueError("OTP key must have the same length as the ciphertext.")

    plaintext = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))

    return plaintext


def main():
    # Provided example keys; do not use these published keys for real secrets.
    plaintext = "HELLO"
    cases = [("Case 1: key equals plaintext length", "XMCKL"),
             ("Case 2: key is shorter than plaintext", "KEY")]

    print("ONE-TIME PAD (ALPHABETIC DEMONSTRATION)")
    print("A real OTP needs a random, independent, secret key used only once.")
    for title, key in cases:
        print("\n" + title)
        print("Plaintext:", plaintext, "| Length:", len(plaintext))
        print("Provided key:", key, "| Length:", len(key))
        try:
            ciphertext = encrypt(plaintext, key)
        except ValueError as error:
            print("Encryption rejected:", error)
            print("Repeating a short key would no longer be a one-time pad.")
            continue

        recovered = decrypt(ciphertext, key)
        print("Ciphertext:", ciphertext)
        print("Decrypted plaintext:", recovered)
        print("Recovered original:", recovered == plaintext.upper())


if __name__ == "__main__":
    main()
