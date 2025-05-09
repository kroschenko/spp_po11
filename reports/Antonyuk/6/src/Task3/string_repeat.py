def repeat(str_: str, separator: str, repeat_count: int) -> str:
    """
    Builds a string from the specified pattern, repeated the specified number of times,
    inserting a separator string at each repetition.

    Args:
        str_: The string to repeat
        separator: The string to insert between repetitions
        repeat_count: The number of times to repeat the string

    Returns:
        The resulting string after repetition

    Raises:
        ValueError: If repeat_count is negative
        TypeError: If str_ or separator is None
    """
    if str_ is None or separator is None:
        raise TypeError("String and separator cannot be None")

    if repeat_count < 0:
        raise ValueError("Repeat count cannot be negative")

    if repeat_count == 0:
        return ""

    # For empty string, handle it specially
    if not str_:
        return separator * (repeat_count - 1)

    # If only one repeat, strip spaces
    if repeat_count == 1:
        return str_.strip()

    # If separator is empty, just concatenate the string repeat_count times
    if not separator:
        return str_ * repeat_count

    # Repeat the string with separator (repeat_count - 1) times
    return (str_ + separator) * (repeat_count - 1) + str_
