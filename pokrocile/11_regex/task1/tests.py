from email_module import validate_email


def test_valid_email():
    assert validate_email("jmeno@email.com") is True


def test_invalid_email():
    assert validate_email("neplatna_adresa") is False
    assert validate_email("chybna@domena") is False


def test_edge_cases():
    assert validate_email("") is False  # Prázdný řetězec není platná e-mailová adresa
    assert validate_email("     ") is False
    assert validate_email("bezZnaku") is False  # Žádný znak '@', není platná e-mailová adresa
    assert validate_email("jmeno@domena.") is False  # Chybějící top-level doména
