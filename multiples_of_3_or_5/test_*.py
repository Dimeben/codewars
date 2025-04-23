from multiples_of_3_or_5 import solution


def test_negative_integer():
    assert solution(-1) == 0
    assert solution(-92347) == 0


def test_positive_integer():
    assert solution(4) == 3
    assert solution(6) == 8
    assert solution(16) == 60
    assert solution(3) == 0
    assert solution(5) == 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(10) == 23
    assert solution(20) == 78
    assert solution(200) == 9168
