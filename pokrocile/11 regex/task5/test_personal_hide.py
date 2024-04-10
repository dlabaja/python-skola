from personal_hide import phone_hide, email_hide


def test_phone_hide():
    persons = ["John: 123-456-7890", "Jane: 987-654-3210", "Mike: 555-123-4567"]
    expected_persons = [
        "John: ***-***-7890",
        "Jane: ***-***-3210",
        "Mike: ***-***-4567",
    ]
    assert phone_hide(persons) == expected_persons


def test_email_hide():
    persons = [
        "Jonatan: jonatan@example.com",
        "Jane: jane.doe@next.cz",
        "Mikie: mikie.smith@tld.org",
    ]
    expected_persons = [
        "Jonatan: j***n@***e.com",
        "Jane: j***e@***t.cz",
        "Mikie: m***h@***d.org",
    ]
    assert email_hide(persons) == expected_persons
