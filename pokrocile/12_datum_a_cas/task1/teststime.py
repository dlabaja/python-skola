import datetime
import pytest
from .task1 import calculate_age


def test_calculate_age():
    date_of_birth = datetime.date(1990, 5, 15)
    assert calculate_age(date_of_birth) == 33  # Assuming current date is 2024-04-17

    date_of_birth = datetime.date(2000, 10, 20)
    assert calculate_age(date_of_birth) == 23  # Assuming current date is 2024-04-17

    date_of_birth = datetime.date(2015, 3, 1)
    assert calculate_age(date_of_birth) == 9  # As
