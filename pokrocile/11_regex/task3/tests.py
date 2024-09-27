from date import find_dates


def test_find_dates():
    text = "Důležitý termín je 15.02.2023 a další je 20.06.2023."
    expected_dates = ['15.02.2023', '20.06.2023']
    actual_dates = find_dates(text)

    assert actual_dates == expected_dates, "Chyba při vyhledávání dat."


def test_not_find_dates():
    text = "Důležitý termín je 69.02.2023 a další je 20.06.2023."
    expected_dates = ['20.06.2023']
    actual_dates = find_dates(text)

    assert actual_dates == expected_dates, "Chyba při vyhledávání dat."
