def two_sum(numbers, target):
    num_to_index = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[number] = index
    return []


N = int(input("Введите количество элементов в массиве: "))

_numbers = []
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    _numbers.append(num)

target_sum = int(input("Введите целевое число: "))

result = two_sum(_numbers, target_sum)
print("Индексы элементов: ", result)
