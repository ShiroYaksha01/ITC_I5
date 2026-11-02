"""Known examples and key-length rules for the two classroom ciphers."""

import unittest

import polyalphabetic_cipher as vigenere
import one_time_pad as otp


class CipherTests(unittest.TestCase):
    def test_equal_length_keys(self):
        for cipher in (vigenere, otp):
            with self.subTest(cipher=cipher.__name__):
                self.assertEqual(cipher.encrypt("HELLO", "XMCKL"), "EQNVZ")
                self.assertEqual(cipher.decrypt("EQNVZ", "XMCKL"), "HELLO")

    def test_vigenere_short_key(self):
        self.assertEqual(vigenere.encrypt("HELLO", "KEY"), "RIJVS")
        self.assertEqual(vigenere.decrypt("RIJVS", "KEY"), "HELLO")

    def test_vigenere_standard_example(self):
        self.assertEqual(vigenere.encrypt("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(vigenere.decrypt("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_otp_rejects_wrong_key_lengths(self):
        for operation in (otp.encrypt, otp.decrypt):
            for key in ("KEY", "XMCKLA"):
                with self.subTest(operation=operation.__name__, key=key):
                    with self.assertRaisesRegex(ValueError, "same length"):
                        operation("HELLO", key)

    def test_lowercase(self):
        for cipher in (vigenere, otp):
            self.assertEqual(cipher.encrypt("hello", "xmckl"), "EQNVZ")
            self.assertEqual(cipher.decrypt("eqnvz", "xmckl"), "HELLO")

    def test_invalid_input(self):
        for cipher in (vigenere, otp):
            for operation in (cipher.encrypt, cipher.decrypt):
                for text, key in (("", "KEY"), ("HELLO", ""),
                                  ("HI!", "KEY"), ("HELLO", "K3Y"),
                                  ("café", "ABCD"), ("ß", "AB")):
                    with self.subTest(cipher=cipher.__name__, text=text, key=key):
                        with self.assertRaises(ValueError):
                            operation(text, key)


if __name__ == "__main__":
    unittest.main()
