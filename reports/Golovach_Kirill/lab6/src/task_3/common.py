def common(str1, str2):
    # Проверка на None
    if str1 is None or str2 is None:
        raise TypeError("Arguments cannot be None")

    # Инициализация переменной для хранения наибольшей общей части
    longest_common = ""

    # Перебор всех возможных подстрок первой строки
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            # Если подстрока найдена во второй строке и она длиннее текущей общей части
            if substring in str2 and len(substring) > len(longest_common):
                longest_common = substring

    return longest_common
