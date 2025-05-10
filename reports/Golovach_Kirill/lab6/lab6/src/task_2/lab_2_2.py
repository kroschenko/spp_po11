def majority_element(nums):
    # Инициализация переменных
    count = 0
    candidate = None

    # Первый проход: находим кандидата на роль элемента большинства
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Второй проход: проверяем, действительно ли candidate является элементом большинства
    # (в данной задаче гарантируется, что элемент большинства существует)
    return candidate


# Примеры использования
if __name__ == "__main__":
    # Тестовые случаи
    nums1 = [3, 2, 3]
    print(majority_element(nums1))  # Output: 3

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(nums2))  # Output: 2
