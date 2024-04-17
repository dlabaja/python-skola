import datetime


def calculate_age(date):
    today = datetime.date(2024, 4, 17)
    return (today - date).days // 365