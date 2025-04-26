"""Module for testing the hamming_distance function."""

import pytest
from .hamming_distance import hamming_distance


def test_both_none_raises_type_error():
    """Test that passing None for both arguments raises a TypeError."""
    with pytest.raises(TypeError):
        hamming_distance(None, None)


def test_first_none_returns_minus_one():
    """Test that passing None as the first argument returns -1."""
    assert hamming_distance(None, "abc") == -1


def test_second_none_returns_minus_one():
    """Test that passing None as the second argument returns -1."""
    assert hamming_distance("abc", None) == -1


def test_different_lengths_raises_value_error():
    """Test that strings of different lengths raise a ValueError."""
    with pytest.raises(ValueError):
        hamming_distance("abc", "abcd")


def test_empty_strings():
    """Test that empty strings return a Hamming distance of 0."""
    assert hamming_distance("", "") == 0


def test_identical_strings():
    """Test that identical strings return a Hamming distance of 0."""
    assert hamming_distance("father", "father") == 0


def test_one_difference():
    """Test that strings with one difference return a Hamming distance of 1."""
    assert hamming_distance("pip", "pop") == 1


def test_two_differences():
    """Test that strings with two differences return a Hamming distance of 2."""
    assert hamming_distance("abcd", "abab") == 2


def test_one_difference_hello():
    """Test that 'hello' and 'hallo' return a Hamming distance of 1."""
    assert hamming_distance("hello", "hallo") == 1


def test_all_different():
    """Test that completely different strings return the correct Hamming distance."""
    assert hamming_distance("abcd", "efgi") == 4
