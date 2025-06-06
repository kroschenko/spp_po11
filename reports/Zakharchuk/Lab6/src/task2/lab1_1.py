def parse_numbers(input_string):
    """Преобразует строку с числами, разделёнными пробелами, в список целых чисел."""
    if not input_string.strip():
        raise ValueError("Все элементы должны быть целыми числами")
    try:
        numbers = list(map(int, input_string.split()))
        if not numbers:
            raise ValueError("Все элементы должны быть целыми числами") from None
        return numbers
    except ValueError as exc:
        raise ValueError("Все элементы должны быть целыми числами") from exc


def calculate_average(numbers):
    """Вычисляет среднее значение списка чисел."""
    if not numbers:
        raise ValueError("Список чисел не может быть пустым")
    return sum(numbers) / len(numbers)


def count_above_average(numbers, average):
    """Подсчитывает количество чисел, больших среднего."""
    return sum(1 for num in numbers if num > average)


def calculate_percentage(count, total):
    """Вычисляет процент от общего количества."""
    if total == 0:
        raise ValueError("Общее количество не может быть нулевым")
    return (count / total) * 100


def main():
    """Основная функция для ввода и вывода."""
    try:
        nums_input = input("Введите числа через пробел: ")
        nums = parse_numbers(nums_input)
        average = calculate_average(nums)
        count = count_above_average(nums, average)
        percent = calculate_percentage(count, len(nums))
        print(f"Среднее значение: {average}")
        print(f"Процент чисел больше среднего: {percent:.2f}%")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
