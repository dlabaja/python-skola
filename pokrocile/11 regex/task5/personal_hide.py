import re


def phone_hide(persons: list[str]) -> list[str]:
    return [re.sub(r"\d{3}-", "***-", person) for person in persons]


def email_hide(persons: list[str]) -> list[str]:
    return [re.sub(r": ([a-z])[a-z.]+([a-z])@[a-z]+([a-z])", r": \1***\2@***\3", person) for person in persons]
