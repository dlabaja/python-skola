import re


def validate_email(email):
    """
    This function checks if the given email address is valid or not.
    :param email: str
    :return: bool
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email))
