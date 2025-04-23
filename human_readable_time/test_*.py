from human_readable_time import make_readable, make_readable_best


def test_human_readable_time():
    assert make_readable(0) == "00:00:00"
    assert make_readable(6) == "00:00:06"
    assert make_readable(59) == "00:00:59"
    assert make_readable(60) == "00:01:00"
    assert make_readable(3599) == "00:59:59"
    assert make_readable(3600) == "01:00:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(86400) == "24:00:00"
    assert make_readable(359999) == "99:59:59"


def test_human_readable_time_best():
    assert make_readable_best(0) == "00:00:00"
    assert make_readable_best(6) == "00:00:06"
    assert make_readable_best(59) == "00:00:59"
    assert make_readable_best(60) == "00:01:00"
    assert make_readable_best(3599) == "00:59:59"
    assert make_readable_best(3600) == "01:00:00"
    assert make_readable_best(86399) == "23:59:59"
    assert make_readable_best(86400) == "24:00:00"
    assert make_readable_best(359999) == "99:59:59"
