from SPP_TASK_1 import process_sequence


def test_normal_sequence():
    """Test with normal sequence of positive numbers"""
    result = process_sequence([1, 2, 3, 4, 5])
    assert result == (5, 1, 15, 120)


def test_negative_numbers():
    """Test with sequence containing negative numbers"""
    result = process_sequence([-1, -2, -3, -4, -5])
    assert result == (-1, -5, -15, -120)


def test_mixed_numbers():
    """Test with sequence containing both positive and negative numbers"""
    result = process_sequence([-1, 2, -3, 4, -5])
    assert result == (4, -5, -3, -120)


def test_single_element():
    """Test with sequence containing single element"""
    result = process_sequence([42])
    assert result == (42, 42, 42, 42)


def test_zero():
    """Test with sequence containing zero"""
    result = process_sequence([0, 1, 2, 3])
    assert result == (3, 0, 6, 0)


def test_empty_sequence():
    """Test with empty sequence"""
    result = process_sequence([])
    assert result == "The sequence is empty"


def test_same_numbers():
    """Test with sequence containing same numbers"""
    result = process_sequence([5, 5, 5, 5])
    assert result == (5, 5, 20, 625)
