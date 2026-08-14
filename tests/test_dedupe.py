from dedupe import dedupe


def test_keeps_first_occurrence_order():
    assert dedupe([3, 1, 2, 1, 3]) == [3, 1, 2]
