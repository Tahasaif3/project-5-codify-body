from discount_cap import apply_discount


def test_normal_discount():
    assert apply_discount(100, 20) == 80.0


def test_discount_over_hundred_percent_caps_at_zero():
    assert apply_discount(100, 150) == 0.0
