def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits  # Если все цифры были 9, добавляем 1 в начало

# Пример использования
digits = list(map(int, input("Введите цифры числа через пробел: ").split()))
print("Результат:", plus_one(digits))
