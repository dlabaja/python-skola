import pytz
import datetime
from workalendar.europe import CzechRepublic
from dateutil.rrule import rrule, DAILY


datum = datetime.datetime.now(pytz.timezone('Europe/Prague'))
print("Aktuální čas v Praze:", datum)


cal = CzechRepublic()
print("Je 16. dubna 2024 pracovní den?", cal.is_working_day(datetime.date(2024, 4, 16)))


start = datetime.datetime(2024, 4, 1)
end = datetime.datetime(2024, 4, 30)
udalosti = rrule(DAILY, dtstart=start, until=end, byweekday=(0, 1, 2, 3, 4))  # Opakující se události od pondělí do pátku
print(list(udalosti))
