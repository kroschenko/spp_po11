import random

def get_positive_integer(prompt):
    """Запрашивает у пользователя положительное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Число должно быть положительным.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def get_numbers_from_user(count):
    """Запрашивает у пользователя ввод чисел."""
    numbers = []
    for i in range(count):
        while True:
            try:
                number = int(input(f"Введите число #{i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Пожалуйста, введите корректное целое число.")
    return numbers

def shuffle_numbers(numbers):
    """Перемешивает числа в случайном порядке."""
    random.shuffle(numbers)
    return numbers

def main():
    # Запрашиваем у пользователя количество чисел N
    N = get_positive_integer("Введите количество чисел (N): ")

    # Запрашиваем у пользователя ввод каждого числа
    numbers = get_numbers_from_user(N)

    # Перемешиваем числа в случайном порядке
    shuffled_numbers = shuffle_numbers(numbers)

    # Выводим числа в случайном порядке
    print("Числа в случайном порядке:")
    print(*shuffled_numbers, sep=", ")

if __name__ == "__main__":
    main()
