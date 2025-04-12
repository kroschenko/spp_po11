def loose(str_value: str, remove: str) -> str:
    """
    Удаляет из первой строки все символы, которые есть во второй строке.
    Также удаляет пробелы в начале и конце строки.

    Args:
        str_value (str): Исходная строка
        remove (str): Строка с символами для удаления

    Returns:
        str: Строка с удаленными символами

    Raises:
        TypeError: Если оба параметра None
    """
    # Проверка на None параметры
    if str_value is None and remove is None:
        raise TypeError("Both parameters cannot be None")
    if str_value is None:
        return None
    if remove is None:
        return str_value

    # Если одна из строк пустая, возвращаем исходную строку
    if not str_value or not remove:
        return str_value

    # Создаем множество символов для удаления для быстрого поиска
    chars_to_remove = set(remove)

    # Фильтруем символы, которые не нужно удалять
    result = "".join(char for char in str_value if char not in chars_to_remove)

    # Удаляем пробелы в начале и конце строки
    return result.strip()
