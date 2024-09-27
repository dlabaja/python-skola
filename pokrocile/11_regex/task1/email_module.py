import re


def validate_email(email):
    if not email:
        return False

    if re.search(r"^[a-zA-Z\d]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}", email):
        return True

    return False
