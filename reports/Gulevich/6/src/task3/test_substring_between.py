import pytest
from substring_between import substringBetween


def test_substringBetween_all_none():
    """Test: substringBetween(None, None, None) = TypeError"""
    with pytest.raises(TypeError):
        substringBetween(None, None, None)


def test_substringBetween_str_none():
    """Test: substringBetween(None, *, *) = None"""
    assert substringBetween(None, "a", "b") is None


def test_substringBetween_open_none():
    """Test: substringBetween(*, None, *) = None"""
    assert substringBetween("abc", None, "b") is None


def test_substringBetween_close_none():
    """Test: substringBetween(*, *, None) = None"""
    assert substringBetween("abc", "a", None) is None


def test_substringBetween_empty_strings():
    """Test: substringBetween('', '', '') = ''"""
    assert substringBetween("", "", "") == ""


def test_substringBetween_empty_with_close():
    """Test: substringBetween('', '', ']') = None"""
    assert substringBetween("", "", "]") is None


def test_substringBetween_empty_with_brackets():
    """Test: substringBetween('', '[', ']') = None"""
    assert substringBetween("", "[", "]") is None


def test_substringBetween_empty_delimiters():
    """Test: substringBetween(' yabcz ', '', '') = ''"""
    assert substringBetween(" yabcz ", "", "") == ""


def test_substringBetween_simple():
    """Test: substringBetween(' yabcz ', 'y', 'z') = ' abc'"""
    assert substringBetween(" yabcz ", "y", "z") == "abc"


def test_substringBetween_multiple():
    """Test: substringBetween(' yabczyabcz ', 'y', 'z') = ' abc '"""
    assert substringBetween(" yabczyabcz ", "y", "z") == "abc"


def test_substringBetween_brackets():
    """Test: substringBetween('wx[b]yz', '[', ']') = 'b'"""
    assert substringBetween("wx[b]yz", "[", "]") == "b"
