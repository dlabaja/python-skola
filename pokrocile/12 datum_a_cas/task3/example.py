from task3_final import StudySchedulePlanner
import datetime

# Example usage:
schedule_planner = StudySchedulePlanner()
schedule_planner.add_subject("Math", "2024-04-20", "10:00:00", "Room 101")
schedule_planner.add_subject("Physics", "2024-04-21", "14:00:00", "Room 201")
schedule_planner.add_subject("Chemistry", "2024-04-22", "09:00:00", "Room 301")

schedule_planner.display_schedule(datetime.datetime(2024, 4, 20), datetime.datetime(2024, 4, 22))
schedule_planner.filter_subjects_by_day("Thursday")
schedule_planner.filter_subjects_by_time(datetime.time(10, 0), datetime.time(15, 0))

schedule_planner.update_subject("Math", "2024-04-20", "11:00:00", "Room 102")
schedule_planner.remove_subject("Physics")