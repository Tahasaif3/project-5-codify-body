from word_count import word_count


def test_single_spaces():
    assert word_count("hello world") == 2


def test_extra_spaces():
    assert word_count("  hello   world  ") == 2
