"""Module for calculating the Hamming distance between two strings."""


def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Hamming distance, or -1 if one string is None.

    Raises:
        TypeError: If both strings are None.
        ValueError: If the strings have different lengths.
    """
    if str1 is None and str2 is None:
        raise TypeError("Both arguments cannot be None")
    if str1 is None or str2 is None:
        return -1
    if len(str1) != len(str2):
        raise ValueError("Strings must have equal length")

    return sum(c1 != c2 for c1, c2 in zip(str1, str2))
