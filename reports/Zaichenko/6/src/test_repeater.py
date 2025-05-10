import pytest
from repeater import repeat_string


def test_spec_e_0():
    assert repeat_string("e", 0) == ""


def test_spec_e_3():
    assert repeat_string("e", 3) == " eee "


def test_spec_abc_2():
    assert repeat_string(" ABC ", 2) == " ABCABC "


def test_spec_e_negative():
    with pytest.raises(ValueError):
        repeat_string("e", -2)


def test_spec_none_1():
    with pytest.raises(TypeError):
        repeat_string(None, 1)


def test_empty_pattern_positive_repeat():
    assert repeat_string("", 5) == "  "


def test_simple_pattern_once():
    assert repeat_string("abc", 1) == " abc "


def test_pattern_with_internal_spaces():
    assert repeat_string("a b", 2) == " a ba b "
