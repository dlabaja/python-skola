import pytest
from .task2 import second_from_midnight


def test_pocet_sekund():
    assert second_from_midnight('00:00:00') == 0
    assert second_from_midnight('01:00:00') == 3600
    assert second_from_midnight('12:00:00') == 43200
    assert second_from_midnight('23:59:59') == 86399
    assert second_from_midnight('10:30:15') == 37815


def test_neplatny_format():
    with pytest.raises(ValueError):
        second_from_midnight('25:00:00')  # Hodiny přesahují 24
    with pytest.raises(ValueError):
        second_from_midnight('12:60:00')  # Minuty přesahují 59
    with pytest.raises(ValueError):
        second_from_midnight('12:00:60')  # Sekundy přesahují 59
    with pytest.raises(ValueError):
        second_from_midnight('12:00')     # Nesprávný formát vstupu
    with pytest.raises(ValueError):
        second_from_midnight('12:00:00:00')  # Nesprávný formát vstupu
