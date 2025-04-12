"""Module for calculating the Hamming weight of positive integers."""


def hamming_weight(n):
    """Calculate the Hamming weight (number of 1s in binary) of a number.

    Args:
        n (int): A positive integer.

    Returns:
        int: The count of 1s in the binary representation of n.
    """
    return bin(n).count("1")


print("Введите количество тестов:")
t = int(input())

print(f"Введите {t} положительных целых чисел (каждое на новой строке):")
for _ in range(t):
    input_n = int(input())
    print(f"Input: n = {input_n}, Output: {hamming_weight(input_n)}")
