plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "MKAYZRDBJCPEOTXFLWVGUSHQNI"


def encrypt(text):
    result = ""

    for char in text.upper():
        if char in plain_alphabet:
            index = plain_alphabet.index(char)
            result += cipher_alphabet[index]
        else:
            result += char

    return result


def decrypt_with_key(text):
    result = ""

    for char in text.upper():
        if char in cipher_alphabet:
            index = cipher_alphabet.index(char)
            result += plain_alphabet[index]
        else:
            result += char

    return result


short_input = "LOG"
long_input = "I LOVE DOING SOMETHING WHIMSY AND FUN"

print("Short Plaintext:", short_input)

ciphertext = encrypt(short_input)
print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypt_with_key(ciphertext))


print("\nLong Plaintext:", long_input)
ciphertext = encrypt(long_input)
print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypt_with_key(ciphertext))