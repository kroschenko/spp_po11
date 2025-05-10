import pytest
from SPP1_2 import is_palindrome

def test_normal_palindrome():
    """Тест обычного палиндрома"""
    assert is_palindrome("А роза упала на лапу Азора") is True

def test_normal_non_palindrome():
    """Тест обычного не-палиндрома"""
    assert is_palindrome("Hello World") is False

def test_empty_string():
    """Тест пустой строки"""
    assert is_palindrome("") is True

def test_single_character():
    """Тест строки из одного символа"""
    assert is_palindrome("a") is True

def test_case_insensitive():
    """Тест на регистронезависимость"""
    assert is_palindrome("Madam") is True

def test_special_characters():
    """Тест со специальными символами"""
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_numbers():
    """Тест с числами"""
    assert is_palindrome("12321") is True

def test_unicode_characters():
    """Тест с Unicode символами"""
    assert is_palindrome("Привет, тевирП") is True

def test_invalid_input():
    """Тест с неверным типом входных данных"""
    with pytest.raises(TypeError, match="Входные данные должны быть строкой"):
        is_palindrome(123)

def test_whitespace():
    """Тест с пробелами"""
    assert is_palindrome("   a   b   a   ") is True

@pytest.mark.parametrize("input_str,expected", [
    ("А роза упала на лапу Азора", True),
    ("Hello World", False),
    ("", True),
    ("a", True),
    ("Madam", True),
    ("A man, a plan, a canal: Panama", True),
    ("12321", True),
    ("Привет, тевирП", True),
    ("   a   b   a   ", True),
])
def test_palindrome_parametrized(input_str, expected):
    """Параметризованный тест для различных случаев"""
    assert is_palindrome(input_str) is expected
