# Daily Calorie Tracker CLI

## Overview
A Python-based Command Line Interface (CLI) application to help you track your daily calorie intake. Input your meals and calories, compare your totals with a personal daily limit, and optionally save session logs for future reference.

## Features
- Log multiple meals and calorie amounts
- Calculate total and average calories consumed
- Warn if daily calorie limit is exceeded
- Display formatted calorie summary
- Save session logs to a text file

## Usage

1. Clone the repository:
git clone https://github.com/shreshthkchaudhary/daily_calorie_tracker_cli.git
2. Navigate to the project folder:
cd daily_calorie_tracker_cli
3. Run the script:
tracker.py

4. Follow the prompts to enter meals, calories, and your daily limit.

## Sample Output
Welcome to the Daily Calorie Tracker!
This tool helps you log your meals, track calorie intake, and compare with your daily limit.

Enter the number of meals you had: 3
Enter name for meal 1: Breakfast
Enter calories for Breakfast: 350
Enter name for meal 2: Lunch
Enter calories for Lunch: 600
Enter name for meal 3: Snack
Enter calories for Snack: 200

Enter your personal daily calorie limit: 1200

Calorie Summary:

Meal Name Calories
Breakfast 350
Lunch 600
Snack 200
Total Calories: 1150.0
Average per Meal: 383.33
Success! Your intake is within the daily limit.

Would you like to save this session to a log file? (yes/no): yes
Session saved to calorie_log.txt


## Requirements
- Python 3.x

## License
This project is for educational purposes only.

---

**Author:** Aditya Raj
**Date:** 9/11/2025
