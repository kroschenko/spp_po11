import pytest

from lab1_2 import generate_pascal_triangle


def test_generate_pascal_triangle_zero_rows():
    assert generate_pascal_triangle(0) == []


def test_generate_pascal_triangle_one_row():
    assert generate_pascal_triangle(1) == [[1]]


def test_generate_pascal_triangle_two_rows():
    assert generate_pascal_triangle(2) == [[1], [1, 1]]


def test_generate_pascal_triangle_three_rows():
    assert generate_pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]


def test_generate_pascal_triangle_five_rows():
    assert generate_pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_generate_pascal_triangle_negative_rows():
    with pytest.raises(ValueError, match="Количество строк не может быть отрицательным"):
        generate_pascal_triangle(-1)
