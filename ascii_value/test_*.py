from ascii_value import get_ascii


def test_ascii_value():
    assert get_ascii("A") == 65
    assert get_ascii("\0") == 0
    assert get_ascii("a") == 97
    assert get_ascii("0") == 48
    assert get_ascii("\n") == 10
