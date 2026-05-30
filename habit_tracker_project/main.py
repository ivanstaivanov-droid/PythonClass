from models import HabitTracker


def print_menu():
    print("\n=== HABIT TRACKER ===")
    print("1. Добави нов навик")
    print("2. Покажи всички навици")
    print("3. Отбележи навик като ИЗПЪЛНЕН")
    print("4. Отбележи навик като ПРОПУСНАТ")
    print("5. Покажи статистика за навик")
    print("0. Изход")


def main():
    tracker = HabitTracker()

    while True:
        print_menu()
        choice = input("Изберете опция: ").strip()

        if choice == "1":
            name = input("Въведете име на навика: ").strip()
            if not name:
                print("Името не може да е празно.")
            else:
                if tracker.add_habit(name):
                    print(f"Навикът '{name}' е добавен.")
                else:
                    print("Такъв навик вече съществува.")

        elif choice == "2":
            habits = tracker.list_habits()
            if not habits:
                print("Няма добавени навици.")
            else:
                print("\nСписък с навици:")
                for i, habit in enumerate(habits, start=1):
                    print(f"{i}. {habit.name} (Изпълнени: {habit.days_done}, Общо: {habit.total_days})")

        elif choice == "3":
            name = input("Кой навик е изпълнен: ").strip()
            habit = tracker.get_habit(name)
            if habit:
                habit.mark_done()
                print(f"'{name}' е отбелязан като изпълнен.")
            else:
                print("Такъв навик няма.")

        elif choice == "4":
            name = input("Кой навик е пропуснат: ").strip()
            habit = tracker.get_habit(name)
            if habit:
                habit.mark_missed()
                print(f"'{name}' е отбелязан като пропуснат.")
            else:
                print("Такъв навик няма.")

        elif choice == "5":
            name = input("Въведете име на навика: ").strip()
            habit = tracker.get_habit(name)
            if habit:
                print(f"\nСтатистика за '{habit.name}':")
                print(f"Изпълнени дни: {habit.days_done}")
                print(f"Общо дни: {habit.total_days}")
                print(f"Успеваемост: {habit.get_success_rate()} %")
            else:
                print("Такъв навик няма.")

        elif choice == "0":
            print("Изход...")
            break

        else:
            print("Невалидна опция.")


if __name__ == "__main__":
    main()
