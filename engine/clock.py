from calendar import month
import random


class Calendar:
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    days = sum(months.values())
    phases = ["Morning", "Afternoon", "Evening", "Night"]

    def month_ranges(months): return [
        ((sum(list(months.values())[: i - 1])), sum(list(months.values())[:i]))
        for i in range(1, len(months) + 1)
    ]
    month_ranges = month_ranges(months)


class Clock:
    PHASE_RATE = 20

    def __init__(self, time=0, calendar=None):
        self.time = time
        self.calendar = calendar or Calendar()
        self.day_rate = self.PHASE_RATE * len(self.calendar.phases)
        self.year_rate = self.day_rate * sum(self.calendar.months.values())

    def tick(self, amount=1):
        self.time += amount

    @ property
    def current_phase(self):
        return int((self.day - int(self.day)) * len(self.calendar.phases))

    @ property
    def day(self):
        return (self.time / self.day_rate) + 1

    @ property
    def phase(self):
        return self.calendar.phases[self.current_phase]

    @ property
    def year(self):
        return (self.time / self.year_rate) + 1

    @ property
    def month(self):
        for i, range_ in enumerate(self.calendar.month_ranges):

            if range_[0] <= self.day_of_year < range_[1]:
                return list(self.calendar.months.keys())[i]

    @ property
    def day_of_year(self):
        return round((self.year - int(self.year)) * self.calendar.days)

    @ property
    def day_of_month(self):
        return (
            self.day_of_year
            - self.calendar.month_ranges[
                list(self.calendar.months.keys()).index(self.month)
            ][0]
            + 1
        )

    @property
    def status(self):
        print(
            f"Today is {self.day_of_month} {self.month}, {int(self.year)}. A pleasant {self.phase}.\n Total ticks: {self.time}\n Total days: {int(self.day)}"
        )


if __name__ == "__main__":
    clock = Clock()
    clock.tick(80)
    print(clock.status)
