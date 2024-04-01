from task4 import complex_word_filter
def test_complex_word_filter():
    # Test na základě předchozího příkladu
    words = ["python", "map", "advanced", "example"]
    expected_result = ['PYTHON1', 'ADVANCED3', 'EXAMPLE3']

    # Zavolejte funkci complex_word_filter
    result = complex_word_filter(words, 5)

    # Porovnejte výsledek s očekávaným výsledkem
    assert result == expected_result, f"Očekáv3áno: {expected_result}, Obdrženo: {result}"