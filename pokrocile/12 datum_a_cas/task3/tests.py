import datetime
import pytest
from .task3 import StudySchedulePlanner


@pytest.fixture
def schedule_planner():
    planner = StudySchedulePlanner()
    planner.add_subject("Math", "2024-04-20", "10:00:00", "Room 101")
    planner.add_subject("Physics", "2024-04-21", "14:00:00", "Room 201")
    planner.add_subject("Chemistry", "2024-04-22", "09:00:00", "Room 301")
    return planner


def test_display_schedule(schedule_planner, capsys):
    schedule_planner.display_schedule(datetime.datetime(2024, 4, 20), datetime.datetime(2024, 4, 22))
    captured = capsys.readouterr()
    assert "Math" in captured.out
    assert "Physics" in captured.out
    assert "Chemistry" in captured.out


def test_filter_subjects_by_day(schedule_planner, capsys):
    schedule_planner.filter_subjects_by_day("Monday")
    captured = capsys.readouterr()
    assert "Chemistry" in captured.out


def test_filter_subjects_by_time(schedule_planner, capsys):
    schedule_planner.filter_subjects_by_time(datetime.time(10, 0), datetime.time(15, 0))
    captured = capsys.readouterr()
    assert "Math" in captured.out
    assert "Physics" in captured.out


def test_update_subject(schedule_planner):
    schedule_planner.update_subject("Math", "2024-04-20", "11:00:00", "Room 102")
    assert schedule_planner.schedule[0].time == datetime.time(11, 00, 00)
    assert schedule_planner.schedule[0].location == "Room 102"


def test_remove_subject(schedule_planner):
    schedule_planner.remove_subject("Physics")
    assert len(schedule_planner.schedule) == 2
    assert "Physics" not in [event.name for event in schedule_planner.schedule]
