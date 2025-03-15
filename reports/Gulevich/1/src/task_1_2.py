def plus_one(digit_list):
    n = len(digit_list)
    for i in range(n - 1, -1, -1):
        if digit_list[i] < 9:
            digit_list[i] += 1
            return digit_list
        digit_list[i] = 0
    return [1] + digit_list  # Если все цифры были 9, добавляем 1 в начало

# Пример использования
example_digit_list = list(map(int, input("Введите цифры числа через пробел: ").split()))
print("Результат:", plus_one(example_digit_list))
