keyword = "QUICKER"
plaintext = "BATTLEHPX"


# 1. Generate 5x5 Key Square

def generate_key_square(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J share one cell

    keyword = keyword.upper().replace("J", "I")

    key_string = ""

    # Add keyword letters without duplicates
    for letter in keyword:
        if letter.isalpha() and letter not in key_string:
            key_string += letter

    # Add remaining alphabet letters
    for letter in alphabet:
        if letter not in key_string:
            key_string += letter

    # Convert into 5x5 matrix
    key_square = []

    for i in range(0, 25, 5):
        key_square.append(list(key_string[i:i + 5]))

    return key_square


# 2. Prepare Plaintext

def prepare_plaintext(text):
    text = text.upper().replace("J", "I")

    cleaned_text = ""

    for letter in text:
        if letter.isalpha():
            cleaned_text += letter

    pairs = []
    repeated_cases = []

    i = 0

    while i < len(cleaned_text):

        first = cleaned_text[i]

        # If only one letter remains
        if i + 1 >= len(cleaned_text):
            second = "X"
            i += 1

        else:
            second = cleaned_text[i + 1]

            # Same Row, Same Column
            # Two identical letters cannot stay in the same pair
            if first == second:

                repeated_cases.append(first + second)

                second = "X"

                # Move only one step so the second repeated
                # letter can be paired again
                i += 1

            else:
                i += 2

        pairs.append(first + second)

    return pairs, repeated_cases


# 3. Find Letter Position

def find_position(key_square, letter):

    if letter == "J":
        letter = "I"

    for row in range(5):
        for col in range(5):

            if key_square[row][col] == letter:
                return row, col


# 4. Encrypt a Pair

def encrypt_pair(pair, key_square):

    first = pair[0]
    second = pair[1]

    row1, col1 = find_position(key_square, first)
    row2, col2 = find_position(key_square, second)

    # Case 1: Same Row, Different Column
    if row1 == row2 and col1 != col2:

        encrypted_first = key_square[row1][(col1 + 1) % 5]
        encrypted_second = key_square[row2][(col2 + 1) % 5]

        rule = "Same Row, Different Column"

    # Case 2: Different Row, Same Column
    elif row1 != row2 and col1 == col2:

        encrypted_first = key_square[(row1 + 1) % 5][col1]
        encrypted_second = key_square[(row2 + 1) % 5][col2]

        rule = "Different Row, Same Column"

    # Case 3: Same Row, Same Column
    elif row1 == row2 and col1 == col2:

        rule = "Same Row, Same Column"

        return pair, rule

    # Case 4: Different Row, Different Column
    else:

        encrypted_first = key_square[row1][col2]
        encrypted_second = key_square[row2][col1]

        rule = "Different Row, Different Column"

    return encrypted_first + encrypted_second, rule


# 5. Main Program

key_square = generate_key_square(keyword)

print("Keyword:", keyword)

print("\n5x5 Key Square:")

for row in key_square:
    print(" ".join(row))


pairs, repeated_cases = prepare_plaintext(plaintext)

print("\nPlaintext:", plaintext)
print("Plaintext Pairs:", " | ".join(pairs))


# Store which pair belongs to each rule
rule_cases = {
    "Same Row, Same Column": [],
    "Same Row, Different Column": [],
    "Different Row, Same Column": [],
    "Different Row, Different Column": []
}


# Add repeated letter cases
for pair in repeated_cases:
    rule_cases["Same Row, Same Column"].append(pair)


ciphertext = ""

print("\nEncryption:")

for pair in pairs:

    encrypted_pair, rule = encrypt_pair(pair, key_square)

    ciphertext += encrypted_pair

    # Store pair under its rule
    rule_cases[rule].append(pair)

    print(
        pair,
        "->",
        encrypted_pair,
        "(" + rule + ")"
    )


print("\nCiphertext:", ciphertext)


# 6. Show Which Pair Uses Each Rule

print("\nRules Covered:")

for rule, pair_list in rule_cases.items():

    if pair_list:
        print(rule + ":", ", ".join(pair_list))

    else:
        print(rule + ": None")