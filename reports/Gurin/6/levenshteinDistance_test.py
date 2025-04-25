import pytest
from levenshteinDistance import levenshteinDistance


def test_null_inputs():
    with pytest.raises(TypeError):
        levenshteinDistance(None, None)
    assert levenshteinDistance(None, "test") == -1
    assert levenshteinDistance("test", None) == -1


def test_empty_strings():
    assert levenshteinDistance("", "") == 0
    assert levenshteinDistance("", "a") == 1
    assert levenshteinDistance(" aaapppp ", "") == 7


def test_strings():
    assert levenshteinDistance(" frog ", " fog ") == 1
    assert levenshteinDistance("fly", " ant ") == 3
    assert levenshteinDistance(" elephant ", " hippo ") == 7
    assert levenshteinDistance(" hippo ", " elephant ") == 7
    assert levenshteinDistance(" hippo ", " zzzzzzzz ") == 8
    assert levenshteinDistance(" hello ", " hallo ") == 1
