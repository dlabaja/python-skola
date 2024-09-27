import datetime


def second_from_midnight(time):
    t = datetime.datetime.strptime(time, "%H:%M:%S")
    return t.hour * 3600 + t.minute * 60 + t.second
