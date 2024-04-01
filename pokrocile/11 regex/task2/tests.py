from password  import validate_password


def test_valid_passwords():
    assert validate_password("Abcd123!") is True
    assert validate_password("StrongP@ss1") is True


def test_invalid_passwords():
    assert validate_password("weakpassword") is False  # Chybí velké písmeno
    assert validate_password("12345678") is False  # Chybí speciální znak
    assert validate_password("NoSpecialChar") is False  # Chybí číslo
    assert validate_password("Short1!") is False  # Heslo je příliš krátké
    assert validate_password("TooLongPassword123456!") is False  # Heslo je příliš dlouhé