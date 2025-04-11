def rep(start_val, end_val, step_val):
    if start_val >= end_val:
        raise ValueError("start должен быть меньше end")

    sequence = []
    current = start_val
    while current < end_val:
        sequence.append(current)
        current += step_val

    return sequence


if __name__ == "__main__":
    try:
        start = int(input("Введите начало последовательности (start): "))
        end = int(input("Введите конец последовательности (end): "))
        step = int(input("Введите шаг последовательности (step): "))

        result = rep(start, end, step)
        print("Сгенерированная последовательность:", result)

    except ValueError as e:
        print("Ошибка:", e)
