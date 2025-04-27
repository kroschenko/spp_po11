import pytest
from repeat import repeat

def test_repeat_zero_times():
    """Тестирование повторения 0 раз."""
    assert repeat("e", "|", 0) == ""

def test_repeat_three_times_with_separator():
    """Тестирование повторения 3 раза с разделителем."""
    assert repeat("e", "|", 3) == "e|e|e"

def test_repeat_with_spaces_and_comma():
    """Тестирование строки с пробелами и запятой как разделителем."""
    assert repeat(" ABC ", ",", 2) == " ABC , ABC "

def test_repeat_with_empty_separator():
    """Тестирование с пустым разделителем."""
    assert repeat(" DBE ", "", 2) == " DBE  DBE "

def test_repeat_once():
    """Тестирование повторения один раз."""
    assert repeat(" DBE ", ":", 1) == " DBE "

def test_repeat_negative_count():
    """Тестирование отрицательного количества повторений."""
    with pytest.raises(ValueError, match="Количество повторений не может быть отрицательным"):
        repeat("e", "|", -2)

def test_repeat_empty_string():
    """Тестирование пустой строки с разделителем."""
    assert repeat("", ":", 3) == "::"

def test_repeat_none_string():
    """Тестирование, когда строка равна None."""
    with pytest.raises(TypeError, match="Строка должна быть типа str, а не NoneType"):
        repeat(None, "a", 1)

def test_repeat_none_separator():
    """Тестирование, когда разделитель равен None."""
    with pytest.raises(TypeError, match="Разделитель должен быть типа str, а не NoneType"):
        repeat("a", None, 2)