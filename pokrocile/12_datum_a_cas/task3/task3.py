import datetime


class StudySchedulePlanner:
    def __init__(self):
        self.schedule = []

    def add_subject(self, name, date, time, location):
        self.schedule.append(PlannedSubject(name, date, time, location))

    def display_schedule(self, start_date, end_date):
        for plan in self.schedule:
            if start_date <= plan.date <= end_date:
                plan.print()

    def filter_subjects_by_day(self, day):
        for plan in self.schedule:
            if plan.date.strftime("%A") == day:
                plan.print()

    def filter_subjects_by_time(self, start_time, end_time):
        for plan in self.schedule:
            if start_time <= plan.time <= end_time:
                plan.print()

    def update_subject(self, name, new_date, new_time, new_location):
        for plan in self.schedule:
            if plan.name == name:
                plan.update(name, new_date, new_time, new_location)
                return

    def remove_subject(self, name):
        for plan in self.schedule:
            if plan.name == name:
                self.schedule.remove(plan)
                return


class PlannedSubject:
    def __init__(self, name, date, time, location):
        self.name = name
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.time = datetime.datetime.strptime(time, "%H:%M:%S").time()
        self.location = location

    def print(self):
        print(f"{self.name} v čase {self.date.strftime('%d.%m.%Y')} "
              f"{self.time.strftime('%H:%M')} v {self.location}")

    def update(self, name, date, time, location):
        self.__init__(name, date, time, location)
