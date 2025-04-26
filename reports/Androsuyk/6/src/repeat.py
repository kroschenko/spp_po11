def repeat(pattern, count):
    if pattern is None:
        raise TypeError("pattern cannot be None")
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count must be non-negative")
    return pattern * count
