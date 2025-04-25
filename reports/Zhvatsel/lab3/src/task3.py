"""Module for encrypting text files using the Strategy pattern."""

import os
from abc import ABC, abstractmethod


class EncryptionStrategy(ABC):
    """Abstract base class for encryption strategies."""

    # pylint: disable=too-few-public-methods

    @abstractmethod
    def encrypt(self, text):
        """Encrypt the input text."""


class RemoveVowelsStrategy(EncryptionStrategy):
    """Strategy to encrypt text by removing vowels."""

    # pylint: disable=too-few-public-methods

    def encrypt(self, text):
        """Remove all vowels from the input text."""
        vowels = set("aeiouAEIOU")
        return "".join(char for char in text if char not in vowels)


class CaesarCipherStrategy(EncryptionStrategy):
    """Strategy to encrypt text using Caesar cipher with a shift."""

    # pylint: disable=too-few-public-methods

    def __init__(self, shift=4):
        self.shift = shift

    def encrypt(self, text):
        """Apply Caesar cipher with specified shift to the input text."""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord("A") if char.isupper() else ord("a")
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result


class XORCipherStrategy(EncryptionStrategy):
    """Strategy to encrypt text using XOR with a key."""

    # pylint: disable=too-few-public-methods

    def __init__(self, key="secret"):
        self.key = key

    def encrypt(self, text):
        """Apply XOR encryption with the specified key to the input text."""
        key_bytes = self.key.encode()
        text_bytes = text.encode()
        result = bytearray()
        for i, byte in enumerate(text_bytes):
            result.append(byte ^ key_bytes[i % len(key_bytes)])
        return result.decode("latin1")


class Encryptor:
    """Class to manage encryption using a specified strategy."""

    # pylint: disable=too-few-public-methods

    def __init__(self, strategy: EncryptionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: EncryptionStrategy):
        """Set the encryption strategy."""
        self.strategy = strategy

    def encrypt(self, text):
        """Encrypt the text using the current strategy."""
        return self.strategy.encrypt(text)


def run_encryption():
    """Prompt user to encrypt a text file using a chosen strategy."""
    while True:
        input_file = input("Enter input file name (e.g., input.txt): ")
        if os.path.isfile(input_file):
            break
        print("File does not exist. Try again.")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading file: {e}")
        return

    print("Available encryption methods:")
    print("1. Remove vowels")
    print("2. Caesar cipher")
    print("3. XOR cipher")

    while True:
        choice = input("Choose method (1-3): ")
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Try again.")

    encryptor = Encryptor(RemoveVowelsStrategy())

    if choice == "1":
        encryptor.set_strategy(RemoveVowelsStrategy())
    elif choice == "2":
        while True:
            try:
                shift = int(input("Enter shift for Caesar cipher (1-25): "))
                if 1 <= shift <= 25:
                    encryptor.set_strategy(CaesarCipherStrategy(shift))
                    break
                print("Shift must be between 1 and 25.")
            except ValueError:
                print("Invalid input. Enter a number.")
    elif choice == "3":
        key = input("Enter key for XOR cipher: ")
        encryptor.set_strategy(XORCipherStrategy(key if key else "secret"))

    encrypted_text = encryptor.encrypt(text)

    output_file = input("Enter output file name (e.g., output.txt): ")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(encrypted_text)
        print(f"Encrypted text written to {output_file}")
        print(f"Encrypted text: {encrypted_text}")
    except (FileNotFoundError, IOError) as e:
        print(f"Error writing file: {e}")


if __name__ == "__main__":
    run_encryption()
