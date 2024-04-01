import re


def find_dates(text):
    matches = re.finditer(r"((0[0-9]|[1-2][0-9]|3[01])\.(0[0-9]|1[0-2]))\.\d{4}", text)
    return list(map(lambda match: match.group(0), matches))
