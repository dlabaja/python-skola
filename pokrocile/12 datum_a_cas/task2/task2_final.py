def second_from_midnight(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    seconds_since_start = hours * 3600 + minutes * 60 + seconds

    return seconds_since_start
