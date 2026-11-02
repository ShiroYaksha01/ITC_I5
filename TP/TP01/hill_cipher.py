from random import randint

from sympy import Matrix

BLOCK_SIZE = 5


# ============================================================
# Convert A-Z into 0-25
# A = 0, B = 1, ..., Z = 25
# ============================================================
def char_to_number(char):
    return ord(char) - ord('A')


# ============================================================
# Convert 0-25 back into A-Z
# 0 = A, 1 = B, ..., 25 = Z
# ============================================================
def number_to_char(number):
    return chr((number % 26) + ord('A'))


# ============================================================
# Create key matrix dynamically
#
# Example for block size 3:
#
# 6 24 1
# 13 16 10
# 20 17 15
#
# ============================================================
def get_key_matrix(size):

    key_matrix = []

    print(f"\nEnter the {size} x {size} key matrix:")
    print(f"Enter {size} numbers from 0 to 25 for each row (separated by spaces).\n")

    for row in range(size):

        while True:

            values = input(f"Row {row + 1}: ").split()

            # Check number of elements
            if len(values) != size:
                print(f"Error: Please enter exactly {size} numbers.")
                continue

            try:
                matrix_row = []

                for value in values:
                    matrix_row.append(int(value))

                if any(value < 0 or value > 25 for value in matrix_row):
                    print("Error: Every number must be from 0 to 25.")
                    continue

                key_matrix.append(matrix_row)
                break

            except ValueError:
                print("Error: Please enter numbers only.")

    return key_matrix


# ============================================================
# Print matrix
# ============================================================
def print_matrix(matrix):

    for row in matrix:

        print("|", end=" ")

        for value in row:
            print(f"{value:3}", end=" ")

        print("|")


# ============================================================
# Matrix × Vector multiplication
#
# Written manually from scratch.
#
# Example:
#
# | a b c |   | x |
# | d e f | × | y |
# | g h i |   | z |
#
# Result:
#
# | ax + by + cz |
# | dx + ey + fz |
# | gx + hy + iz |
#
# Every result is mod 26.
# ============================================================
def multiply_matrix_vector(matrix, vector):

    size = len(matrix)

    result = []

    for row in range(size):

        total = 0

        for column in range(size):

            total = total + (
                matrix[row][column] * vector[column]
            )

        # Hill Cipher works modulo 26
        total = total % 26

        result.append(total)

    return result


# ============================================================
# Prepare plaintext
#
# - Convert to uppercase
# - Remove spaces
# - Remove non-alphabetic characters
# - Add X padding if needed
# ============================================================
def prepare_plaintext(plaintext, block_size):

    plaintext = plaintext.upper()

    cleaned_text = ""

    for char in plaintext:

        if char.isalpha():
            cleaned_text += char

    # Add X until plaintext is divisible by block size
    while len(cleaned_text) % block_size != 0:
        cleaned_text += "X"

    return cleaned_text


# ============================================================
# Convert block of letters into number vector
#
# Example:
#
# HELLO
#
# H = 7
# E = 4
# L = 11
# L = 11
# O = 14
#
# [7, 4, 11, 11, 14]
# ============================================================
def block_to_vector(block):

    vector = []

    for char in block:

        number = char_to_number(char)

        vector.append(number)

    return vector


# ============================================================
# Convert number vector back into letters
#
# Example:
#
# [7, 4, 11, 11, 14]
#
# becomes
#
# HELLO
# ============================================================
def vector_to_block(vector):

    block = ""

    for number in vector:

        block += number_to_char(number)

    return block


# ============================================================
# Encrypt
#
# Formula:
#
# C = K × P mod 26
#
# C = Ciphertext vector
# K = Key matrix
# P = Plaintext vector
# ============================================================
def encrypt(plaintext, key_matrix, block_size):

    plaintext = prepare_plaintext(
        plaintext,
        block_size
    )

    ciphertext = ""

    print("\n========================================")
    print("ENCRYPTION")
    print("========================================")

    print("\nPrepared Plaintext:", plaintext)

    block_number = 1

    for start in range(0, len(plaintext), block_size):

        # Get one block
        block = plaintext[
            start:start + block_size
        ]

        # Convert letters into numbers
        plaintext_vector = block_to_vector(block)

        # Encrypt:
        # C = K × P mod 26
        cipher_vector = multiply_matrix_vector(
            key_matrix,
            plaintext_vector
        )

        # Convert encrypted numbers back into letters
        cipher_block = vector_to_block(
            cipher_vector
        )

        print(f"\nBlock {block_number}")

        print("Plaintext:")
        print(block)

        print("Plaintext Vector:")
        print(plaintext_vector)

        print("Ciphertext Vector:")
        print(cipher_vector)

        print("Ciphertext:")
        print(cipher_block)

        ciphertext += cipher_block

        block_number += 1

    return ciphertext


# ============================================================
# Get inverse/reversed key matrix
#
# EXISTING LIBRARY IS USED ONLY HERE.
#
# We need:
#
# K^-1 mod 26
#
# A normal matrix inverse is NOT enough because
# Hill Cipher works modulo 26.
# ============================================================
def get_inverse_matrix(key_matrix):

    matrix = Matrix(key_matrix)

    try:

        inverse = matrix.inv_mod(26)

    except Exception:

        return None

    # Convert SymPy Matrix into normal Python list
    inverse_matrix = []

    for row in range(inverse.rows):

        current_row = []

        for column in range(inverse.cols):

            value = int(inverse[row, column]) % 26

            current_row.append(value)

        inverse_matrix.append(current_row)

    return inverse_matrix


# ============================================================
# Decrypt
#
# Formula:
#
# P = K^-1 × C mod 26
#
# P    = Plaintext vector
# K^-1 = Inverse key matrix
# C    = Ciphertext vector
# ============================================================
def decrypt(ciphertext, inverse_matrix, block_size):

    plaintext = ""

    print("\n========================================")
    print("DECRYPTION")
    print("========================================")

    block_number = 1

    for start in range(0, len(ciphertext), block_size):

        # Get one ciphertext block
        block = ciphertext[
            start:start + block_size
        ]

        # Convert ciphertext letters to numbers
        cipher_vector = block_to_vector(block)

        # Decrypt:
        # P = K^-1 × C mod 26
        plaintext_vector = multiply_matrix_vector(
            inverse_matrix,
            cipher_vector
        )

        # Convert numbers back into letters
        plaintext_block = vector_to_block(
            plaintext_vector
        )

        print(f"\nBlock {block_number}")

        print("Ciphertext:")
        print(block)

        print("Ciphertext Vector:")
        print(cipher_vector)

        print("Plaintext Vector:")
        print(plaintext_vector)

        print("Plaintext:")
        print(plaintext_block)

        plaintext += plaintext_block

        block_number += 1

    return plaintext


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    while True:
        try:
            runs = int(input("How many times do you want to run the Hill cipher? "))
            if runs > 0:
                break
        except ValueError:
            pass
        print("Please enter a positive whole number.")

    for run in range(1, runs + 1):
        print(f"\nRun {run} of {runs}")
        print("========================================")
        print("           HILL CIPHER")
        print("========================================")


        # ------------------------------------------------------------
        # 1. Use a fixed block of five plaintext letters
        # ------------------------------------------------------------

        block_size = BLOCK_SIZE

        print(
            f"\nBlock size = {block_size}"
        )

        print(
            f"Therefore, key matrix must be "
            f"{block_size} x {block_size}"
        )


        # ------------------------------------------------------------
        # 3. Get key matrix from user
        # ------------------------------------------------------------

        while True:
            mode = input("\nKey input: 1 = manual, 2 = auto generate (0-25): ").strip().lower()
            if mode in ("1", "manual"):
                key_matrix = get_key_matrix(block_size)
            elif mode in ("2", "auto"):
                while True:
                    key_matrix = [
                        [randint(0, 25) for _ in range(block_size)]
                        for _ in range(block_size)
                    ]
                    if get_inverse_matrix(key_matrix) is not None:
                        break
            else:
                print("Please choose 1 (manual) or 2 (auto).")
                continue

            if get_inverse_matrix(key_matrix) is not None:
                break
            print("This key has no inverse modulo 26. Please choose another key.")


        print("\nKey Matrix:")

        print_matrix(
            key_matrix
        )


        # ------------------------------------------------------------
        # 4. Find inverse key matrix
        #
        # Library is allowed for this part.
        # ------------------------------------------------------------

        inverse_matrix = get_inverse_matrix(
            key_matrix
        )


        # Check if matrix has inverse modulo 26
        if inverse_matrix is None:

            print("\nERROR!")

            print(
                "This key matrix does not have "
                "an inverse modulo 26."
            )

            print(
                "Please choose another key matrix."
            )

        else:

            print("\nInverse Key Matrix (mod 26):")

            print_matrix(
                inverse_matrix
            )


            # --------------------------------------------------------
            # 5. Get plaintext
            # --------------------------------------------------------

            while True:
                plaintext = input(
                    f"\nEnter Plaintext ({BLOCK_SIZE} letters): "
                )

                if len(plaintext) != BLOCK_SIZE:
                    print(f"Plaintext must contain exactly {BLOCK_SIZE} letters.")
                    continue

                if not plaintext.isascii() or not plaintext.isalpha():
                    print("Plaintext must contain A-Z letters only.")
                    continue

                plaintext = plaintext.upper()
                break


            # --------------------------------------------------------
            # 6. Encrypt
            # --------------------------------------------------------

            ciphertext = encrypt(
                plaintext,
                key_matrix,
                block_size
            )


            print("\n========================================")

            print(
                "Final Ciphertext:",
                ciphertext
            )


            # --------------------------------------------------------
            # 7. Decrypt
            # --------------------------------------------------------

            decrypted_text = decrypt(
                ciphertext,
                inverse_matrix,
                block_size
            )


            print("\n========================================")

            print(
                "Final Decrypted Plaintext:",
                decrypted_text
            )

            print("========================================")


if __name__ == "__main__":
    main()
