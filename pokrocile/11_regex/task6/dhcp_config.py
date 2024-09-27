import re


def check_dhcp_config(line: str) -> bool:
    return re.search(r"([a-z]*\.[a-z]*\.[a-z]*\s*ha=[0-9a-fA-F]{12}:ip=[\d]+\.[\d]+\.[\d]+\.[\d]+:)", line) is not None


def transfer_dhcp_config(text: str) -> str:
    return re.sub(
        r"([a-z]*\.[a-z]*\.[a-z]*)\s*ha=([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2}):ip=(\d+\.\d+\.\d+\.\d+)",
        r"\nhost \1 {\nlink address \2:\3:\4:\5:\6:\7;\n fix  address \8;\n}\n", text)
