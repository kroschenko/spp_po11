def repeat(string, separator, repeat_count):
    if string is None:
        raise TypeError("Строка должна быть типа str, а не NoneType")
    if separator is None:
        raise TypeError("Разделитель должен быть типа str, а не NoneType")
    if not isinstance(string, str) or not isinstance(separator, str):
        raise TypeError("Строка и разделитель должны быть типа str")
    if repeat_count < 0:
        raise ValueError("Количество повторений не может быть отрицательным")
    if repeat_count == 0:
        return ""
    if repeat_count == 1:
        return string
    return separator.join([string] * repeat_count)
