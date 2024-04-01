from task1 import transform_words


def test_transform_words():
    words = ["python", "map", "advanced", "example"]
    expected_result = ['PYTHON6', 'MAP3', 'ADVANCED8', 'EXAMPLE7']

    result = transform_words(words)

    assert result == expected_result, f"Očekáváno: {expected_result}, Obdrženo: {result}"