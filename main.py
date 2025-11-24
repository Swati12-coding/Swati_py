
import json
import datetime
import os

DATA_FILE = 'habits.json'

def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_habits(habits):
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f, indent=4)

def add_habit(habits):
    name = input("Enter habit name: ").strip()
    if name in habits:
        print("Habit already exists.")
        return
    habits[name] = {
        "created": str(datetime.date.today()),
        "streak": 0,
        "last_completed": None
    }
    save_habits(habits)
    print(f"Habit '{name}' added.")

def mark_habit_done(habits):
    name = input("Enter habit name to mark done: ").strip()
    if name not in habits:
        print("Habit not found.")
        return
    today = datetime.date.today()
    last_completed_str = habits[name]["last_completed"]
    if last_completed_str:
        last_completed = datetime.datetime.strptime(last_completed_str, "%Y-%m-%d").date()
        if last_completed == today:
            print("Habit already marked done today.")
            return
        elif last_completed == today - datetime.timedelta(days=1):
            habits[name]["streak"] += 1
        else:
            habits[name]["streak"] = 1
    else:
        habits[name]["streak"] = 1
    habits[name]["last_completed"] = str(today)
    save_habits(habits)
    print(f"Habit '{name}' marked done. Current streak: {habits[name]['streak']}")

def view_habits(habits):
    if not habits:
        print("No habits found.")
        return
    print(f"{'Habit':20} {'Created':12} {'Last Done':12} {'Streak'}")
    print("-"*50)
    for name, data in habits.items():
        print(f"{name:20} {data['created']:12} {str(data['last_completed']):12} {data['streak']}")

def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Mark Habit Done")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Choose option (1-4): ").strip()
        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            mark_habit_done(habits)
        elif choice == '3':
            view_habits(habits)
        elif choice == '4':
            print("Exiting habit tracker.")
            break
        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()
