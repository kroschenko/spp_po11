def two_sum(nums, target):
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i
    
    return []

N = int(input("Введите количество элементов в массиве: "))

nums = []
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    nums.append(num)

target = int(input("Введите целевое число: "))

result = two_sum(nums, target)
print("Индексы элементов:", result)
