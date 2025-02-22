def check_sequence(sequence):
    if all(x == sequence[0] for x in sequence):
        return "равны"
    else:
        return "не равны"


N = int(input("Введите длину последовательности: "))

_sequence = []
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    _sequence.append(element)

result = check_sequence(_sequence)
print(f"Элементы последовательности: {result}.")
