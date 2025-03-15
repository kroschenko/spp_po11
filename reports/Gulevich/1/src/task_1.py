def find_median(numbers):
    numbers.sort()  # Сортируем список чисел
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]  # Возвращаем средний элемент, если количество нечетное
    mid1, mid2 = numbers[n // 2 - 1], numbers[n // 2]
    return (mid1 + mid2) / 2  # Возвращаем среднее двух средних элементов

sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
print("Медиана:", find_median(sequence))
