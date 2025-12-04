# Name: Aditya Raj
# Date: 9/11/2025
# Project Title: Daily Calorie Tracker CLI

# Task 1: Setup & Introduction
print("\nWelcome to the Daily Calorie Tracker!\nThis tool helps you log your meals, track calorie intake, and compare with your daily limit.\n")

# Task 2: Input & Data Collection
meal_name = []
calorie_amount = []
total_meals = int(input("Enter the number of meals you had: "))
for i in range(total_meals):
    meal = input(f"Enter name for meal {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_name.append(meal)
    calorie_amount.append(calories)

# Task 3: Calorie Calculations
total_calories = sum(calorie_amount)
average_calories = total_calories / total_meals
daily_limit = float(input("\nEnter your personal daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    limit_status = "Warning: You have exceeded your daily limit!"
else:
    limit_status = "Success! Your intake is within the daily limit."

# Task 5: Neatly Formatted Output
print("\nCalorie Summary:\n")
print("{:<20} {:<10}".format("Meal Name","Calories"))
print("-"*30)
for meal, cal in zip(meal_name, calorie_amount):
    print("{:<20} {:<10}".format(meal, str(cal)))
print("-"*30)
print(f"Total Calories:  {total_calories}")
print(f"Average per Meal:  {average_calories:.2f}")
print(limit_status)

# Task 6 (Bonus): Save Session Log to File
save_log = input("\nWould you like to save this session to a log file? (yes/no): ")
if save_log.lower() == "yes":
    with open("calorie_log.txt", "w") as f:
        f.write("Meal Name\tCalories\n")
        for meal, cal in zip(meal_name, calorie_amount):
            f.write(f"{meal}\t{cal}\n")
        f.write(f"Total Calories:\t{total_calories}\n")
        f.write(f"Average per Meal:\t{average_calories:.2f}\n")
        f.write(f"Daily Limit:\t{daily_limit}\n")
        f.write(f"{limit_status}\n")
    print("Session saved to calorie_log.txt")