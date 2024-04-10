import re


def pick_numbers(text: str) -> list[int]:
    nums = re.findall(r"\d+", text.replace(" ", "").replace("\t", ""))
    return [int(num) for num in nums]
