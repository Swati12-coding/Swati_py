# Project Proposal: Digital Habit Tracker Application

##  Problem Statement

The primary challenge for individuals aiming to build or break habits is **consistency and accountability**. People often rely on manual, inconsistent methods (like paper lists or simple calendar entries) which lack effective tracking, motivational feedback, and progress visualization. This leads to high rates of abandonment shortly after starting a new habit, as they lose sight of their long-term progress and motivation. The current tools fail to integrate seamlessly into a daily routine while providing intelligent, adaptive nudges.

---

##  Scope of the Project (Habit Tracker MVP)

This project focuses on developing a **Minimum Viable Product (MVP)** for a cross-platform mobile application that helps users track, manage, and visualize their daily habits.

### Inclusions (What the Project Will Deliver):
* A Python-based Command-Line Interface (CLI) application.
* Data persistence using a local JSON file (habits.json).
* A single-user environment with no authentication required.
* Core habit management functions: Add, Mark Done, and View.
* Calculation of the current daily success streak (incrementing if completed yesterday, resetting otherwise).
  
### Exclusions (What the Project Will *Not* Deliver in MVP):
* Any form of Graphical User Interface (GUI), web interface, or mobile application.
* Multi-user support, cloud synchronization, or external database integration.
* Advanced features like reminder notifications, historical data visualization, or habit frequency customization (all habits are assumed to be daily).
* Data export functionality beyond viewing in the terminal.

---

##  Target Users

### Primary Users: Motivated Individuals (Ages 18-45)
* **Goal:** Establish consistency in key areas (fitness, reading, learning a new skill) and maintain long-term streaks.
* **Need:** A straightforward, visually rewarding way to check off tasks and see progress immediately.

### Secondary Users: Casual Users and Students
* **Goal:** Track mandatory tasks (like homework or chores) or low-priority personal development goals.
* **Need:** Simplicity and quick logging without complex setup.

---

## 🌟 High-Level Features

### 1. Habit Creation and Configuration
* Allow users to define a new habit (e.g., "Drink 8 glasses of water," "Meditate for 10 minutes").
* Users can set the required frequency (daily, specific days of the week, or X times per week) and preferred time.

### 2. Daily Tracking and Completion
* A clean, intuitive dashboard showing all current habits due for the day.
* Simple one-tap action to mark a habit as complete.
* Automatic calculation and display of the current successful streak length for each habit.

### 3.Basic Streak Calculation
* Feature: Automatically updates the success count.

* Functionality: Checks if the habit was completed exactly the day before (i.e., maintaining the chain) to increment the streak, or resets the streak if a day was missed.


### 4. Habit Listing and Status View
* Feature: Display a formatted list of all tracked habits.

* Information Displayed: Habit Name, Date Created, Date Last Completed, and Current Streak Length.
 
