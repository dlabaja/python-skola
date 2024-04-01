from task2 import filter_numbers_greater_than_five


def test_filter_numbers_greater_than_five():
    numbers = [3, 8, 1, 6, 4, 7, 2, 9]
    expected_result = [8, 6, 7, 9]

    # Zavolejte funkci filter_numbers_greater_than_five
    result = filter_numbers_greater_than_five(numbers)

    # Porovnejte výsledek s očekávaným výsledkem
    assert result == expected_result, f"Očekáváno: {expected_result}, Obdrženo: {result}"
