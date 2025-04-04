def rep(start, end, step):
    if start >= end:
        raise ValueError("start должен быть меньше end")

    sequence = []
    current = start
    while current < end:
        sequence.append(current)
        current += step
    
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
    