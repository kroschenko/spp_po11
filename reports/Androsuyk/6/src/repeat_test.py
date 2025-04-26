import pytest
from repeat import repeat


def test_repeat_zero():
    assert repeat("e", 0) == ""


def test_repeat_positive():
    assert repeat("e", 3) == "eee"
    assert repeat(" ABC ", 2) == " ABC  ABC "


def test_repeat_negative():
    with pytest.raises(ValueError):
        repeat("e", -2)


def test_repeat_none_pattern():
    with pytest.raises(TypeError):
        repeat(None, 1)


def test_repeat_empty_pattern():
    assert repeat("", 5) == ""
