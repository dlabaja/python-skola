import re

def find_dates(text):
    dates = re.findall(r'\d{2}.\d{2}.\d{4}', text)
    return dates