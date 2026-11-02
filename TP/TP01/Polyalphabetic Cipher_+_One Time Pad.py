import secrets

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clean(text):
    return text.upper().replace(" ", "")


def valid(text):
    return len(text) > 0 and all("A" <= ch <= "Z" for ch in text)


def generate_key(length):
    key = ""
    for _ in range(length):
        key += ALPHABET[secrets.randbelow(26)]
    return key


def repeat_key(key, length):
    full_key = ""
    for i in range(length):
        full_key += key[i % len(key)]
    return full_key


def show_numbers(name, text):
    numbers = []
    for letter in text:
        numbers.append(str(ord(letter) - ord("A")))
    print(f"{name}: {text} -> [" + ", ".join(numbers) + "]")


def encrypt(plaintext, full_key):
    ciphertext = ""
    print("\nENCRYPTION: C_i = (P_i + K_i) mod 26")

    for i in range(len(plaintext)):
        p_letter = plaintext[i]
        k_letter = full_key[i]

        p = ord(p_letter) - ord("A")
        k = ord(k_letter) - ord("A")
        total = p + k
        c = total % 26
        c_letter = chr(c + ord("A"))

        print(
            f"{p_letter} + {k_letter} = ({p} + {k}) mod 26 = "
            f"{total} mod 26 = {c} = {c_letter}"
        )

        ciphertext += c_letter

    return ciphertext


def decrypt(ciphertext, full_key):
    plaintext = ""
    print("\nDECRYPTION: P_i = (C_i - K_i + 26) mod 26")

    for i in range(len(ciphertext)):
        c_letter = ciphertext[i]
        k_letter = full_key[i]

        c = ord(c_letter) - ord("A")
        k = ord(k_letter) - ord("A")
        difference = c - k + 26
        p = difference % 26
        p_letter = chr(p + ord("A"))

        print(
            f"{c_letter} - {k_letter} = ({c} - {k} + 26) mod 26 = "
            f"{difference} mod 26 = {p} = {p_letter}"
        )

        plaintext += p_letter

    return plaintext


def read_generated_key_length(message_length):
    length_text = input(
        f"Key length (1-{message_length}, Enter = {message_length}): "
    ).strip()

    if not length_text:
        return message_length

    if not length_text.isdecimal():
        raise SystemExit("Error: key length must be a number.")

    key_length = int(length_text)
    if not 1 <= key_length <= message_length:
        raise SystemExit(
            f"Error: key length must be 1-{message_length}."
        )

    return key_length


def select_key(message_length):
    print("\nKey options:")
    print("1. Auto-generate a key")
    print("2. Enter a key manually")
    option = input("Choose 1 or 2: ").strip()

    if option == "1":
        key_length = read_generated_key_length(message_length)
        return generate_key(key_length), "Generated"

    if option == "2":
        key = clean(input("Enter key: "))

        if not valid(key):
            raise SystemExit("Error: key must contain only A-Z.")

        if len(key) > message_length:
            raise SystemExit(
                "Error: key cannot be longer than plaintext."
            )

        return key, "Provided"

    raise SystemExit("Error: choose 1 or 2.")


def read_generated_key_length(message_length):
    length_text = input(
        f"Key length (1-{message_length}, Enter = {message_length}): "
    ).strip()

    if not length_text:
        return message_length

    if not length_text.isdecimal():
        raise SystemExit("Error: key length must be a number.")

    key_length = int(length_text)
    if not 1 <= key_length <= message_length:
        raise SystemExit(
            f"Error: key length must be 1-{message_length}."
        )

    return key_length


def select_key(message_length):
    print("\nKey options:")
    print("1. Auto-generate a key")
    print("2. Enter a key manually")
    option = input("Choose 1 or 2: ").strip()

    if option == "1":
        key_length = read_generated_key_length(message_length)
        return generate_key(key_length), "Generated"

    if option == "2":
        key = clean(input("Enter key: "))

        if not valid(key):
            raise SystemExit("Error: key must contain only A-Z.")

        if len(key) > message_length:
            raise SystemExit(
                "Error: key cannot be longer than plaintext."
            )

        return key, "Provided"

    raise SystemExit("Error: choose 1 or 2.")


def main():
    message = clean(input("Enter plaintext: "))

    if not valid(message):
        raise SystemExit("Error: plaintext must contain only A-Z.")

    key, key_source = select_key(len(message))

    if len(key) == len(message):
        mode = "Same-length key"
    else:
        mode = "Short key repeated (Vigenere cipher)"

    full_key = repeat_key(key, len(message))

    print(f"\nMode: {mode}")
    print(f"Key source: {key_source}")
    print(
        f"Lengths: plaintext = {len(message)}, "
        f"original key = {len(key)}"
    )
    print(f"Plaintext: {message}")
    print(f"Given/generated key: {key}")
    print(f"Key used: {full_key}")

    print("\nConvert letters to numbers (A=0, ..., Z=25):")
    show_numbers("P", message)
    show_numbers("K", full_key)

    ciphertext = encrypt(message, full_key)
    print(f"Therefore, ciphertext = {ciphertext}")
    show_numbers("C", ciphertext)

    recovered = decrypt(ciphertext, full_key)
    print(f"Therefore, plaintext = {recovered}")
    print("Decryption correct:", recovered == message)


if __name__ == "__main__":
    main()