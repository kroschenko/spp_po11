import pytest
from keep import keep

def test_both_none():
    with pytest.raises(TypeError):
        keep(None, None)

def test_first_none():
    assert keep(None, "abc") is None

def test_empty_string():
    assert keep("", "abc") == ""

def test_pattern_none():
    assert keep("abc", None) == ""

def test_pattern_empty():
    assert keep("abc", "") == ""

def test_keep_hl():
    assert keep(" hello ", "hl") == " hll "

def test_keep_le():
    assert keep(" hello ", "le") == " ell "
