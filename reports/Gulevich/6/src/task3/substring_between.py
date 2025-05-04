def substringBetween(str_val, open_str, close_str):
    """
    Выделяет подстроку между открывающей и закрывающей строками.

    Args:
        str_val (str): Исходная строка
        open_str (str): Открывающая строка
        close_str (str): Закрывающая строка

    Returns:
        str или None: Подстрока между открывающей и закрывающей строками,
                     или None, если подстрока не найдена или параметры некорректны

    Raises:
        TypeError: Если все параметры None
    """
    # Проверка на все None
    if str_val is None and open_str is None and close_str is None:
        raise TypeError()

    # Проверка на None в любом из параметров
    if str_val is None or open_str is None or close_str is None:
        return None

    # Проверка на пустые строки
    if str_val == "" and (open_str != "" or close_str != ""):
        return None

    # Если все разделители пустые
    if open_str == "" and close_str == "":
        return str_val if str_val == "" else ""

    # Поиск индексов
    start = str_val.find(open_str)
    if start == -1:
        return None

    # Начинаем поиск закрывающей строки после открывающей
    start_pos = start + len(open_str)
    end = str_val.find(close_str, start_pos)
    if end == -1:
        return None

    # Возвращаем подстроку между разделителями
    return str_val[start_pos:end]
