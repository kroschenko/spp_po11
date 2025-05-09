import random

def main():
    # Запрашиваем у пользователя количество чисел N
    try:
        N = int(input("Введите количество чисел (N): "))
        if N <= 0:
            print("Количество чисел должно быть положительным.")
            return
    except ValueError:
        print("Пожалуйста, введите целое число.")
        return

    # Создаем список для хранения чисел
    numbers = []

    # Запрашиваем у пользователя ввод каждого числа
    for i in range(N):
        while True:
            try:
                number = int(input(f"Введите число #{i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Пожалуйста, введите корректное целое число.")

    # Перемешиваем числа в случайном порядке
    random.shuffle(numbers)

    # Выводим числа в случайном порядке
    print("Числа в случайном порядке:")
    print(*numbers, sep=", ")

if __name__ == "__main__":
    main()
