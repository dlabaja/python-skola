from datetime import datetime, timedelta


class Event:
    def __init__(self, description, time):
        self.description = description
        self.time = time


class EventTimeline:
    def __init__(self):
        self.events = []

    def add_event(self, description, time):
        event = Event(description, time)
        self.events.append(event)
        self.events.sort(key=lambda x: x.time)

    def __len__(self):
        return len(self.events)

    def __getitem__(self, index):
        return self.events[index]

    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        if self.position < len(self.events):
            event = self.events[self.position]
            self.position += 1
            return event
        else:
            raise StopIteration

    def __str__(self):
        return "\n".join([f"{event.description} - {event.time}" for event in self.events])

# Creating an instance of the class
timeline = EventTimeline()

# Adding events
timeline.add_event("Meeting", datetime(2024, 2, 1, 14, 0))
timeline.add_event("Lunch with friends", datetime(2024, 2, 1, 12, 30))
timeline.add_event("Presentation", datetime(2024, 2, 2, 10, 0))

# Iterating through the object using a for loop
print("Timeline:")
for event in timeline:
    print(event.description, "-", event.time)

# Displaying the length of the timeline
print("\nTimeline length:", len(timeline))

# Accessing events using an index
print("\nFirst event:", timeline[0].description, "-", timeline[0].time)

# Displaying the timeline as a string
print("\nTimeline as a string:")
print(timeline)
