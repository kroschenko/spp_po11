def indexOfDifference(str1, str2):
    """
    Сравнивает две строки и возвращает индекс позиции, в которой они различаются.

    :param str1: Первая строка
    :param str2: Вторая строка
    :return: Индекс различия или -1, если строки полностью совпадают
    :raises TypeError: Если оба аргумента равны None
    """
    # Проверка на None
    if str1 is None and str2 is None:
        raise TypeError("Оба аргумента не могут быть None")

    # Обрезаем пробелы в начале и конце строк
    str1 = str1.strip()
    str2 = str2.strip()

    # Определяем минимальную длину для итерации
    min_length = min(len(str1), len(str2))

    # Ищем первую позицию, где символы не совпадают
    for i in range(min_length):
        if str1[i] != str2[i]:
            return i

    # Если строки совпадают до конца одной из них
    if len(str1) != len(str2):
        return min_length

    # Если строки полностью совпадают
    return -1
