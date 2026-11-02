def encrypt_caesar(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt_caesar(message, key):
    return encrypt_caesar(message, -key)


plaintext = "Hello, World!"
print("Original Message:", plaintext)

encrypted_message = encrypt_caesar(plaintext, 3)
print("Encrypted Message:", encrypted_message)
decrypted_message = decrypt_caesar(encrypted_message, 3)
print("Decrypted Message:", decrypted_message)