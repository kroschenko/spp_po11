def keep(input_str, pattern):
    if input_str is None and pattern is None:
        raise TypeError("Both arguments cannot be None")
    if input_str is None:
        return None
    if pattern is None:
        return ""
    if not input_str or not pattern:
        return ""
    keep_chars = set(pattern)
    result = []
    for char in input_str:
        if char in keep_chars or char.isspace():
            result.append(char)
    return "".join(result)
