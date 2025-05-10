import pytest
from string_repeat import repeat


def test_basic_repeat():
    """Test basic repeat functionality"""
    assert repeat("e", "|", 3) == "e|e|e"


def test_zero_repeat():
    """Test with zero repeat count"""
    assert repeat("e", "|", 0) == ""


def test_with_spaces():
    """Test with spaces in string"""
    assert repeat(" ABC ", ",", 2) == " ABC , ABC "


def test_empty_separator():
    """Test with empty separator"""
    assert repeat(" DBE ", "", 2) == " DBE  DBE "


def test_single_repeat():
    """Test with single repeat"""
    assert repeat(" DBE ", ":", 1) == "DBE"


def test_negative_repeat():
    """Test with negative repeat count"""
    with pytest.raises(ValueError):
        repeat("e", "|", -2)


def test_empty_string():
    """Test with empty string"""
    assert repeat("", ":", 3) == "::"


def test_none_string():
    """Test with None as string"""
    with pytest.raises(TypeError):
        repeat(None, "a", 1)


def test_none_separator():
    """Test with None as separator"""
    with pytest.raises(TypeError):
        repeat("a", None, 2)


def test_large_repeat():
    """Test with large repeat count"""
    result = repeat("a", "b", 1000)
    assert len(result) == 1999  # 1000 'a's and 999 'b's
    assert result.count("a") == 1000
    assert result.count("b") == 999
