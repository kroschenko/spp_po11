import pytest
from string_utils import keep

def test_keep_none_none():
    with pytest.raises(TypeError):
        keep(None, None)

def test_keep_none_pattern():
    assert keep(None, "abc") is None

def test_keep_empty_str():
    assert keep("", "abc") == ""

def test_keep_str_none():
    assert keep("hello", None) == ""

def test_keep_empty_pattern():
    assert keep("hello", "") == ""

def test_keep_hello_hl():
    assert keep(" hello ", "hl ") == " hll "

def test_keep_hello_le():
    assert keep(" hello ", "le ") == " ell "

def test_keep_special_chars():
    assert keep("a1!b2@c3#", "123!@#") == "1!2@3#"

def test_keep_no_matches():
    assert keep("hello", "xyz") == ""
