def repeat_string(pattern, count):
    if not isinstance(count, int):
        raise TypeError("Count must be an integer.")

    if pattern is None and count > 0:
        raise TypeError("Pattern cannot be None if count is positive.")

    if not isinstance(pattern, str) and count > 0 and pattern is not None:
        raise TypeError("Pattern must be a string.")

    if count < 0:
        raise ValueError("Count cannot be negative.")

    if count == 0:
        return ""

    core_pattern = ""
    if pattern is not None:
        core_pattern = pattern.strip()

    repeated_core = core_pattern * count

    return " " + repeated_core + " "
