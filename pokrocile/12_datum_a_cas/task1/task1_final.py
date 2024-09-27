import datetime


def calculate_age(date):
    today = datetime.date.today()
    birth_date = date.replace(year=today.year)

    if birth_date > today:
        return today.year - date.year - 1
    else:
        return today.year - date.year
