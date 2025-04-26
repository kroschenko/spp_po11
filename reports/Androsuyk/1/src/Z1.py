def check_sequence(sequence):
    if not sequence:
        return "пустая последовательность"
    if all(x == sequence[0] for x in sequence):
        return "равны"
    return "не равны"


if __name__ == "__main__":
    N = int(input("Введите длину последовательности: "))

    _sequence = []
    for i in range(N):
        element = int(input(f"Введите элемент {i + 1}: "))
        _sequence.append(element)

    result = check_sequence(_sequence)
    print(f"Элементы последовательности: {result}.")
