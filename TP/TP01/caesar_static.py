# Convert a letter to a number
def letter_to_number(char):
    return ord(char.upper()) - ord('A')


# Convert a number back to a letter
def number_to_letter(number):
    return chr((number % 26) + ord('A'))



# 1. STATIC CAESAR CIPHER
# C = (P - 5) mod 26

def static_encrypt(plaintext):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            P = letter_to_number(char)

            # C = (P - 5) mod 26
            C = (P - 5) % 26

            ciphertext += number_to_letter(C)
        else:
            ciphertext += char

    return ciphertext


def static_decrypt(ciphertext):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            C = letter_to_number(char)

            # Reverse:
            # C = P - 5
            # P = C + 5
            P = (C + 5) % 26

            plaintext += number_to_letter(P)
        else:
            plaintext += char

    return plaintext

# Test
message = "LEGEND"

print("Plaintext:", message)

print("\n--- Static Caesar Cipher ---")

static_cipher = static_encrypt(message)
print("Ciphertext:", static_cipher)

static_plain = static_decrypt(static_cipher)
print("Decrypted Plaintext:", static_plain)
