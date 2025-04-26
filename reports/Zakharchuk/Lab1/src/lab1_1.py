# Ввод чисел от пользователя
nums = input("Введите числа через пробел: ")

# Преобразуем строку в список чисел
nums = list(map(int, nums.split()))

# Находим среднее значение
average = sum(nums) / len(nums)

# Подсчитываем, сколько чисел больше среднего
count = 0
for num in nums:
    if num > average:
        count += 1

# Вычисляем процент
percent = (count / len(nums)) * 100

# Вывод результата
print(f"Среднее значение: {average}")
print(f"Процент чисел больше среднего: {percent:.2f}%")
