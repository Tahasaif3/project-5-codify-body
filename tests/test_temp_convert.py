from temp_convert import fahrenheit_to_celsius


def test_freezing_point():
    assert fahrenheit_to_celsius(32) == 0.0


def test_boiling_point():
    assert fahrenheit_to_celsius(212) == 100.0
