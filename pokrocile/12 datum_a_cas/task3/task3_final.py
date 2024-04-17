import datetime


class StudySchedulePlanner:
    def __init__(self):
        self.schedule = []

    def add_subject(self, name, date, time, location):
        self.schedule.append({"name": name, "date": date, "time": time, "location": location})

    def display_schedule(self, start_date, end_date):
        print("Study Schedule:")
        for event in self.schedule:
            event_date = datetime.datetime.strptime(event['date'], '%Y-%m-%d')
            if start_date <= event_date <= end_date:
                print(f"Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}")

    def filter_subjects_by_day(self, day):
        print(f"Subjects for {day}:")
        for event in self.schedule:
            event_date = datetime.datetime.strptime(event['date'], '%Y-%m-%d')
            if event_date.strftime("%A") == day:
                print(f"Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}")

    def filter_subjects_by_time(self, start_time, end_time):
        print(f"Subjects between {start_time} and {end_time}:")
        for event in self.schedule:
            event_time = datetime.datetime.strptime(event['time'], '%H:%M:%S').time()
            if start_time <= event_time <= end_time:
                print(f"Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Location: {event['location']}")

    def update_subject(self, name, new_date, new_time, new_location):
        for event in self.schedule:
            if event['name'] == name:
                event['date'] = new_date
                event['time'] = new_time
                event['location'] = new_location
                print(f"Subject {name} updated.")

    def remove_subject(self, name):
        self.schedule = [event for event in self.schedule if event['name'] != name]
        print(f"Subject {name} removed.")

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
