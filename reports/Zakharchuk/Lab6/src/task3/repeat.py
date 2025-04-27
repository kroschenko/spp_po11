def repeat_string(string, separator, count):
    """Повторяет строку заданное количество раз с указанным разделителем."""
    if string is None:
        raise TypeError("Строка должна быть типа str, а не NoneType")
    if separator is None:
        raise TypeError("Разделитель должен быть типа str, а не NoneType")
    if not isinstance(string, str) or not isinstance(separator, str):
        raise TypeError("Строка и разделитель должны быть типа str")
    if count < 0:
        raise ValueError("Количество повторений не может быть отрицательным")
    if count == 0:
        return ""
    if count == 1:
        return string
    return separator.join([string] * count)