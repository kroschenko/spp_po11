import pytest
from task_2 import binary_addition


def test_trivial_cases():
    assert binary_addition(1, 2) == "11"
    assert binary_addition(1, 2, 3) == "110"


def test_boundary_cases():
    assert binary_addition(0, 0) == "0"
    assert binary_addition(5) == "101"
    assert binary_addition(1000) == bin(1000)[2:]


def test_negative_numbers():
    with pytest.raises(TypeError):
        binary_addition(-1, 2)


def test_non_numeric_input():
    with pytest.raises(TypeError):
        binary_addition("a", 2)


def test_empty_input():
    assert binary_addition() == "0"


def test_float_input():
    with pytest.raises(TypeError):
        binary_addition(1.5, 2)
