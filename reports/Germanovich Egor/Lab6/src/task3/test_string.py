import pytest
from string_utils import loose


def test_loose_none_none():
    """Тест на оба None параметра"""
    with pytest.raises(TypeError):
        loose(None, None)


def test_loose_none_any():
    """Тест на первый параметр None"""
    assert loose(None, "abc") is None


def test_loose_empty_any():
    """Тест на пустую первую строку"""
    assert loose("", "abc") == ""


def test_loose_any_none():
    """Тест на второй параметр None"""
    assert loose("abc", None) == "abc"


def test_loose_any_empty():
    """Тест на пустую вторую строку"""
    assert loose("abc", "") == "abc"


def test_loose_hello_hl():
    """Тест на удаление символов 'h' и 'l' из строки ' hello '"""
    assert loose(" hello ", "hl") == "eo"


def test_loose_hello_le():
    """Тест на удаление символов 'l' и 'e' из строки ' hello '"""
    assert loose(" hello ", "le") == "ho"


# Дополнительные тесты для проверки граничных случаев
def test_loose_same_string():
    """Тест на удаление всех символов"""
    assert loose("abc", "abc") == ""


def test_loose_no_common_chars():
    """Тест на отсутствие общих символов"""
    assert loose("abc", "def") == "abc"


def test_loose_duplicate_chars():
    """Тест на удаление дублирующихся символов"""
    assert loose("aabbcc", "ab") == "cc"


def test_loose_whitespace():
    """Тест на удаление пробелов"""
    assert loose("a b c", " ") == "abc"


def test_loose_special_chars():
    """Тест на удаление специальных символов"""
    assert loose("a!b@c#", "!@#") == "abc"
