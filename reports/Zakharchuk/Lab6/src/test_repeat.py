import pytest

from repeat import repeat


def test_repeat_zero_times():
    assert repeat("e", "|", 0) == ""


def test_repeat_three_times_with_separator():
    assert repeat("e", "|", 3) == "e|e|e"


def test_repeat_with_spaces_and_comma():
    assert repeat(" ABC ", ",", 2) == " ABC , ABC "


def test_repeat_with_empty_separator():
    assert repeat(" DBE ", "", 2) == " DBE  DBE "


def test_repeat_once():
    assert repeat(" DBE ", ":", 1) == " DBE "


def test_repeat_negative_count():
    with pytest.raises(ValueError, match="Количество повторений не может быть отрицательным"):
        repeat("e", "|", -2)


def test_repeat_empty_string():
    assert repeat("", ":", 3) == "::"


def test_repeat_none_string():
    with pytest.raises(TypeError, match="Строка должна быть типа str, а не NoneType"):
        repeat(None, "a", 1)


def test_repeat_none_separator():
    with pytest.raises(TypeError, match="Разделитель должен быть типа str, а не NoneType"):
        repeat("a", None, 2)
