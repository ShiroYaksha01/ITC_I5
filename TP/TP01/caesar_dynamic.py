# Convert a letter to a number
def letter_to_number(char):
    return ord(char.upper()) - ord('A')


# Convert a number back to a letter
def number_to_letter(number):
    return chr((number % 26) + ord('A'))


# 2. DYNAMIC CAESAR CIPHER
# C(i) = (P(i) + 6 - 5i^2) mod 26
# Initial key = 6; letter positions start at i = 0.

def dynamic_encrypt(plaintext):
    ciphertext = ""
    i = 0

    for char in plaintext:
        if char.isalpha():
            P = letter_to_number(char)

            # C(i) = (P(i) + 6 - 5i^2) mod 26
            C = (P + 6 - 5 * (i ** 2)) % 26

            ciphertext += number_to_letter(C)

            i += 1
        else:
            ciphertext += char

    return ciphertext


def dynamic_decrypt(ciphertext):
    plaintext = ""
    i = 0

    for char in ciphertext:
        if char.isalpha():
            C = letter_to_number(char)

            # Reverse: P(i) = (C(i) - 6 + 5i^2) mod 26
            P = (C - 6 + 5 * (i ** 2)) % 26

            plaintext += number_to_letter(P)

            i += 1
        else:
            plaintext += char

    return plaintext


# ============================================================
# TEST
# ============================================================
message = "LEGEND"
print("Plaintext:", message)

print("\n--- Dynamic Caesar Cipher ---")


dynamic_cipher = dynamic_encrypt(message)
print("Ciphertext:", dynamic_cipher)

dynamic_plain = dynamic_decrypt(dynamic_cipher)
print("Decrypted Plaintext:", dynamic_plain)
