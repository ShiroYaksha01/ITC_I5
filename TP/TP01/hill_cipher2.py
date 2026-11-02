from sympy import Matrix

BLOCK_SIZE = 5


def char_to_number(char):
    return ord(char) - ord('A')


def number_to_char(number):
    return chr((number % 26) + ord('A'))


# User dynamically enters the 5 x 5 key matrix
def get_key_matrix():
    key_matrix = []

    print(f"Enter the {BLOCK_SIZE} x {BLOCK_SIZE} key matrix:")

    for i in range(BLOCK_SIZE):

        while True:
            row = input(f"Row {i + 1}: ").split()

            if len(row) != BLOCK_SIZE:
                print(f"Enter exactly {BLOCK_SIZE} numbers.")
                continue

            try:
                row = [int(value) % 26 for value in row]
                key_matrix.append(row)
                break

            except ValueError:
                print("Enter numbers only.")

    return key_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Matrix multiplication written from scratch
def multiply_matrix_vector(matrix, vector):

    result = []

    for i in range(BLOCK_SIZE):

        total = 0

        for j in range(BLOCK_SIZE):
            total += matrix[i][j] * vector[j]

        result.append(total % 26)

    return result


def text_to_vector(text):

    vector = []

    for char in text:
        vector.append(char_to_number(char))

    return vector


def vector_to_text(vector):

    text = ""

    for number in vector:
        text += number_to_char(number)

    return text


def encrypt_block(plaintext, key_matrix):

    plaintext = plaintext.upper()

    plaintext_vector = text_to_vector(plaintext)

    cipher_vector = multiply_matrix_vector(
        key_matrix,
        plaintext_vector
    )

    ciphertext = vector_to_text(cipher_vector)

    return plaintext_vector, cipher_vector, ciphertext


def get_inverse_matrix(key_matrix):

    # Existing library used only for reversed/inverse matrix
    matrix = Matrix(key_matrix)

    try:
        inverse = matrix.inv_mod(26)

    except Exception:
        return None

    inverse_matrix = []

    for i in range(BLOCK_SIZE):

        row = []

        for j in range(BLOCK_SIZE):
            row.append(int(inverse[i, j]) % 26)

        inverse_matrix.append(row)

    return inverse_matrix


def decrypt_block(ciphertext, inverse_matrix):

    cipher_vector = text_to_vector(ciphertext)

    plaintext_vector = multiply_matrix_vector(
        inverse_matrix,
        cipher_vector
    )

    plaintext = vector_to_text(plaintext_vector)

    return cipher_vector, plaintext_vector, plaintext


# ==========================================================
# MAIN
# ==========================================================

print("===================================")
print("          HILL CIPHER")
print("===================================")

print(f"\nFixed Block Size: {BLOCK_SIZE}")
print(f"Key Matrix Size : {BLOCK_SIZE} x {BLOCK_SIZE}")


# Get matrix from user
key_matrix = get_key_matrix()

print("\nKey Matrix:")
print_matrix(key_matrix)


# Find inverse matrix
inverse_matrix = get_inverse_matrix(key_matrix)

if inverse_matrix is None:

    print("\nError:")
    print("The key matrix cannot be inverted modulo 26.")

else:

    print("\nInverse Key Matrix:")
    print_matrix(inverse_matrix)


    # Get exactly 5 plaintext letters
    while True:

        plaintext = input(
            f"\nEnter Plaintext ({BLOCK_SIZE} letters): "
        )

        if len(plaintext) != BLOCK_SIZE:
            print(
                f"Plaintext must contain exactly "
                f"{BLOCK_SIZE} letters."
            )
            continue

        if not plaintext.isascii() or not plaintext.isalpha():
            print("Plaintext must contain A-Z letters only.")
            continue

        plaintext = plaintext.upper()
        break


    # Encryption
    plaintext_vector, cipher_vector, ciphertext = encrypt_block(
        plaintext,
        key_matrix
    )

    print("\n========== ENCRYPTION ==========")

    print("Plaintext       :", plaintext)
    print("Plaintext Vector:", plaintext_vector)
    print("Ciphertext Vector:", cipher_vector)
    print("Ciphertext      :", ciphertext)


    # Decryption
    cipher_vector, decrypted_vector, decrypted_text = decrypt_block(
        ciphertext,
        inverse_matrix
    )

    print("\n========== DECRYPTION ==========")

    print("Ciphertext      :", ciphertext)
    print("Ciphertext Vector:", cipher_vector)
    print("Plaintext Vector:", decrypted_vector)
    print("Decrypted Plaintext:", decrypted_text)