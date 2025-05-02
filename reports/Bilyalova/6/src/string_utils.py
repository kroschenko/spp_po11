def keep(str_, pattern):
    if str_ is None and pattern is None:
        raise TypeError("Both arguments cannot be None")
    if str_ is None:
        return None
    if str_ == "" or pattern is None or pattern == "":
        return ""
    keep_chars = set(pattern)
    return "".join(char for char in str_ if char in keep_chars)
