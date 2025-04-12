def calculate_negative_squares_sum(numbers_list):
    """
    Вычисляет сумму квадратов отрицательных чисел из списка.

    Args:
        numbers_list (list): Список чисел (целых или дробных)

    Returns:
        float: Сумма квадратов отрицательных чисел
    """
    return sum(x**2 for x in numbers_list if x < 0)


def main():
    try:
        numbers = input("Введите числа через пробел: ")
        # Используем float вместо int для поддержки дробных чисел
        numbers_list = list(map(float, numbers.split()))
        sum_of_squares = calculate_negative_squares_sum(numbers_list)
        print("Сумма квадратов всех отрицательных чисел:", sum_of_squares)
    except ValueError:
        print("Ошибка: введите корректные числа через пробел")


if __name__ == "__main__":
    main()
