def filter_numbers_greater_than_five(numbers):
    filter_condition = lambda x: x > 5
    filtered_numbers = filter(filter_condition, numbers)
    return list(filtered_numbers)

