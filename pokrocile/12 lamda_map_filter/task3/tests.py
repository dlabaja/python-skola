from task3 import add_initials

def test_add_initials():
    # Příklad s inicialy
    people = [
        {"name": "John", "surname": "Doe"},
        {"name": "Alice", "surname": "Smith"},
        {"name": "Bob", "surname": "Johnson"},
    ]

    expected_result = [
        {"name": "John", "surname": "Doe", "initials": "JD"},
        {"name": "Alice", "surname": "Smith", "initials": "AS"},
        {"name": "Bob", "surname": "Johnson", "initials": "BJ"},
    ]

    result = add_initials(people)

    assert result == expected_result, f"Očekáváno: {expected_result}, Obdrženo: {result}"

