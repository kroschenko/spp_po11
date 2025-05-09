"""Module for testing the count_digits_distribution function."""

from .task1 import count_digits_distribution


def test_empty_sequence():
    """Test that an empty sequence returns an empty dictionary."""
    assert not count_digits_distribution([])  # Simplified: empty dict is falsy


def test_single_number():
    """Test that a single number returns the correct digit count."""
    assert count_digits_distribution([123]) == {3: 1}


def test_multiple_numbers():
    """Test that multiple numbers return the correct digit distribution."""
    assert count_digits_distribution([1, 12, 123, 1234]) == {1: 1, 2: 1, 3: 1, 4: 1}


def test_negative_numbers():
    """Test that negative numbers are handled correctly."""
    assert count_digits_distribution([-12, -123]) == {2: 1, 3: 1}


def test_zero():
    """Test that zero is counted as having one digit."""
    assert count_digits_distribution([0]) == {1: 1}


def test_large_number():
    """Test that a large number returns the correct digit count."""
    assert count_digits_distribution([1000000]) == {7: 1}
