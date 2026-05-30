class Habit:
    def __init__(self, name):
        self.name = name
        self.days_done = 0
        self.total_days = 0

    def mark_done(self):
        self.days_done += 1
        self.total_days += 1

    def mark_missed(self):
        self.total_days += 1

    def get_success_rate(self):
        if self.total_days == 0:
            return 0.0
        return round((self.days_done / self.total_days) * 100, 2)


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        if self.get_habit(name) is not None:
            return False
        habit = Habit(name)
        self.habits.append(habit)
        return True

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
        return None

    def list_habits(self):
        return self.habits
