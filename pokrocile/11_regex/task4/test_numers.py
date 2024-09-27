from pick_numbers import pick_numbers


def test_pick_numbers():
    text = """10, 22, 18 1 ;11  : 87 ,   12
19:33  ;   44 55
123 456
"""
    excepted_numbers = [10, 22, 181, 11, 87, 12, 19, 33, 4455, 123456]

    assert excepted_numbers == pick_numbers(text)
