"""Module for counting digit distribution in a sequence of numbers."""


def count_digits_distribution(sequence):
    """Count the number of digits in each number of the sequence.

    Args:
        sequence (list): A list of integers.

    Returns:
        dict: A dictionary mapping the number of digits to their frequency.
    """
    distribution = {}
    for num in sequence:
        digits = len(str(abs(num)))
        distribution[digits] = distribution.get(digits, 0) + 1
    return distribution


if __name__ == "__main__":
    print("Введите количество чисел в последовательности:")
    n = int(input())
    input_sequence = []
    print(f"Введите {n} целых чисел (каждое на новой строке):")
    for _ in range(n):
        input_num = int(input())
        input_sequence.append(input_num)
    result = count_digits_distribution(input_sequence)
    for num_digits, count in sorted(result.items()):
        print(f"Чисел с {num_digits} цифрой(ами): {count}")
