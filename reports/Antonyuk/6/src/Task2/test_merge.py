from SPP_TASK_2 import merge


def test_basic_merge():
    """Test basic merge functionality"""
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    merge(num1, 3, num2, 3)
    assert num1 == [1, 2, 2, 3, 5, 6]


def test_empty_num2():
    """Test when num2 is empty"""
    num1 = [1, 2, 3]
    num2 = []
    merge(num1, 3, num2, 0)
    assert num1 == [1, 2, 3]


def test_empty_num1():
    """Test when num1 has no elements (only zeros)"""
    num1 = [0, 0, 0]
    num2 = [1, 2, 3]
    merge(num1, 0, num2, 3)
    assert num1 == [1, 2, 3]


def test_all_same_number():
    """Test with all same numbers"""
    num1 = [1, 1, 1, 0, 0, 0]
    num2 = [1, 1, 1]
    merge(num1, 3, num2, 3)
    assert num1 == [1, 1, 1, 1, 1, 1]


def test_negative_numbers():
    """Test with negative numbers"""
    num1 = [-3, -2, -1, 0, 0, 0]
    num2 = [-2, 0, 2]
    merge(num1, 3, num2, 3)
    assert num1 == [-3, -2, -2, -1, 0, 2]


def test_different_sizes():
    """Test with different sizes"""
    num1 = [1, 2, 3, 4, 0, 0]
    num2 = [5, 6]
    merge(num1, 4, num2, 2)
    assert num1 == [1, 2, 3, 4, 5, 6]


def test_num2_larger_elements():
    """Test when all elements in num2 are larger"""
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [4, 5, 6]
    merge(num1, 3, num2, 3)
    assert num1 == [1, 2, 3, 4, 5, 6]


def test_num2_smaller_elements():
    """Test when all elements in num2 are smaller"""
    num1 = [4, 5, 6, 0, 0, 0]
    num2 = [1, 2, 3]
    merge(num1, 3, num2, 3)
    assert num1 == [1, 2, 3, 4, 5, 6]
