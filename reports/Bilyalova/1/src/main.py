from collections import Counter


def find_modes(input_sequence):
    counts = Counter(input_sequence)
    max_count = max(counts.values())

    if max_count == 1:
        return None

    modes_list = [num for num, count in counts.items() if count == max_count]

    return modes_list


try:
    n = int(input("Введите количество чисел в последовательности: "))
    sequence = []
    for i in range(n):
        num = int(input(f"Введите число {i + 1}: "))
        sequence.append(num)

    modes = find_modes(sequence)

    if modes is None:
        print("В последовательности нет моды")
    else:
        print("Мода последовательности:", ", ".join(map(str, modes)))
except ValueError:
    print("Ошибка: введите целые числа.")
