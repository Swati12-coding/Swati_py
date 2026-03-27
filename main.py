
 import json
import datetime
import os
import random

DATA_FILE = 'habits.json'

def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_habits(habits):
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f, indent=4)

def ai_suggest_habit(habits):
    suggestions = [
        "Drink 2L water daily",
        "Exercise for 20 minutes",
        "Read 10 pages",
        "Meditate for 5 minutes",
        "Sleep before 11 PM",
        "Practice coding for 1 hour"
    ]

    print("\n🤖 AI Habit Suggestions:")
    
    for habit in habits:
        if "exercise" in habit.lower():
            print("👉 You already exercise. Try adding: 'Stretching'")
        elif "read" in habit.lower():
            print("👉 You read. Try adding: 'Note-taking habit'")

    print("👉 General Suggestions:")
    for s in random.sample(suggestions, 2):
        print("-", s)

def ai_motivation(streak):
    if streak == 0:
        return "Start today 💪 Every big success begins small!"
    elif streak < 3:
        return "Good start 🔥 Keep going!"
    elif streak < 7:
        return "You're building momentum 🚀"
    else:
        return "Amazing consistency 🧠 You're unstoppable!"

def ai_analyze_progress(habits):
    print("\n📊 AI Analysis Report:")

    if not habits:
        print("No data to analyze.")
        return

    total = len(habits)
    active = sum(1 for h in habits.values() if h["streak"] > 0)

    print(f"Total habits: {total}")
    print(f"Active habits: {active}")

    if active / total > 0.7:
        print("🔥 Excellent consistency!")
    elif active / total > 0.4:
        print("👍 Good, but can improve.")
    else:
        print("⚠️ Try to focus on fewer habits and stay consistent.")

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

    # AI Suggestion after adding habit
    ai_suggest_habit(habits)

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

    streak = habits[name]["streak"]

    print(f"Habit '{name}' marked done. Current streak: {streak}")

    # AI Motivation
    print("🤖 AI says:", ai_motivation(streak))

def view_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print(f"{'Habit':20} {'Created':12} {'Last Done':12} {'Streak'}")
    print("-"*50)

    for name, data in habits.items():
        print(f"{name:20} {data['created']:12} {str(data['last_completed']):12} {data['streak']}")

    # AI Analysis
    ai_analyze_progress(habits)

# ------------------ MAIN ------------------

def main():
    habits = load_habits()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Mark Habit Done")
        print("3. View Habits")
        print("4. AI Suggestions")
        print("5. Exit")

        choice = input("Choose option (1-5): ").strip()

        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            mark_habit_done(habits)
        elif choice == '3':
            view_habits(habits)
        elif choice == '4':
            ai_suggest_habit(habits)
        elif choice == '5':
            print("Exiting habit tracker.")
            break
        else:
            print("Invalid choice. Try again.")

# FIXED BUG HERE
if __name__ == "__main__":
    main()
   
   
       
