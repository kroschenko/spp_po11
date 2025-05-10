import os
import sys
import pytest
from lab1_2 import isPalindrome

current_dir = os.path.dirname(os.path.abspath(__file__))
lab1_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "1", "src"))
sys.path.append(lab1_dir)


@pytest.mark.parametrize("s, expected", [
    ("121", True),
    ("12321", True),
    ("1", True),
    ("0", True),
    ("11", True),
    ("999", True),
    ("101", True),
    ("1221", True),
    ("10", False),
    ("123", False),
    ("100", False),
    ("12345", False),
])
def test_isPalindrome_numbers_as_strings(s, expected):
    assert isPalindrome(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("", True),
    ("a", True),
    ("aa", True),
    ("aba", True),
])
def test_isPalindrome_letter_strings(s, expected):
    assert isPalindrome(s) == expected


@pytest.mark.parametrize("s, expected", [
    ("a1a", True),
    ("1a1", True),
    (" ", True),
    ("  ", True),
    ("!@!", True),
    ("a!b!a", True),
    ("a!b!!b!a", True),
])
def test_isPalindrome_mixed_strings(s, expected):
    assert isPalindrome(s) == expected


def test_isPalindrome_empty_string():
    assert isPalindrome("") is True


def test_isPalindrome_single_character():
    assert isPalindrome("x") is True
    assert isPalindrome("7") is True
    assert isPalindrome("[") is True
