"""Module for testing the hamming_weight function."""

import pytest

from .task2 import hamming_weight


def test_zero():
    """Test that the Hamming weight of zero is zero."""
    assert hamming_weight(0) == 0


def test_positive_number():
    """Test that the Hamming weight of a positive number (11) is correct."""
    assert hamming_weight(11) == 3  # 11 = 1011 in binary


def test_power_of_two():
    """Test that the Hamming weight of a power of two (16) is correct."""
    assert hamming_weight(16) == 1  # 16 = 10000 in binary


def test_large_number():
    """Test that the Hamming weight of a large number (2^32 - 1) is correct."""
    assert hamming_weight(4294967295) == 32  # 2^32 - 1, all bits 1


def test_negative_number_raises_error():
    """Test that a negative number raises a ValueError."""
    with pytest.raises(ValueError):
        hamming_weight(-1)
