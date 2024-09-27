import re

text = "Včera bylo 25 stupňů Celsia a dnes je 30 stupňů Celsia."
numbers = re.findall(r'\b\d+\b', text)

print("Nalezená čísla:", numbers)


text = "Python je skvělý jazyk. Python je mocný. Python je oblíbený."
modified_text = re.sub(r'Python', 'JavaScript', text)

print("Modifikovaný text:", modified_text)


text = "Toto je příklad použití regulárních výrazů v Pythonu."
words = re.findall(r'\b\w+\b', text)

print("Seznam slov:", words)


text = "Navštivte náš web na adrese https://www.example.com"
urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print("Nalezené URL:", urls)


def validate_ico(ico):
    return bool(re.match(r'^\d{8}$', ico))

validate_ico("12345678")  # True
validate_ico("1234567")  # False
validate_ico("123456789")  # False
validate_ico("1234567a")  # False