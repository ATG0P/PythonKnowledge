import pandas as pd

# Creating the Daily Habit Tracker
daily_habits = [
    "🏋️‍♂️ Workout (as per split)",
    "💧 Drank 3L+ water",
    "🍽️ Ate clean meals (low oil/sugar)",
    "🥚 Hit protein target (~110g)",
    "🧃 Took Whey Protein (1 scoop)",
    "⚡ Took Creatine (5g)",
    "🧴 Washed face 2x/day",
    "🚿 No-soap bath (Besan/Neem)",
    "👕 Changed gym clothes after workout",
    "🛌 Slept 7+ hours",
    "📸 Took progress pic (every 7 days)"
]

# Creating the Weekly Workout Plan
weekly_workout = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Focus": ["Chest + Cardio", "Shoulders + Core", "Back + Cardio", "Arms (Bi + Tri)", "Chest + Core", "Back + Shoulders + Walk", "Rest + Grooming"]
}

# Creating the Supplement Guide
supplement_guide = {
    "Supplement": ["Whey Protein", "Creatine Monohydrate"],
    "Timing": ["Post-Workout", "Anytime (preferably Post-Workout)"],
    "Dosage": ["1 Scoop (~30g)", "5g Daily"],
    "With What": ["Water (250 ml)", "Water or mix with whey"]
}

# Creating the sample meal plan
meal_plan = {
    "Time": ["Breakfast", "Lunch", "Snack", "Dinner", "Optional Night"],
    "Meal": [
        "4 eggs or paneer bhurji + 1 roti + fruit",
        "Sabzi + 1.5 cups rice + curd + 2 eggs or chicken",
        "1 boiled egg + banana + black coffee",
        "2 rotis + sabzi + 1 egg/paneer",
        "Milk + almonds"
    ]
}

# Creating the Progress Journal Template
progress_journal = {
    "Week": list(range(1, 9)),
    "Weight (kg)": ["" for _ in range(8)],
    "Waist (inches)": ["" for _ in range(8)],
    "Skin Condition": ["" for _ in range(8)],
    "Energy/Mood": ["" for _ in range(8)],
    "Notes": ["" for _ in range(8)]
}

# Create dataframes
df_daily = pd.DataFrame({"Daily Habit": daily_habits})
df_workout = pd.DataFrame(weekly_workout)
df_supplements = pd.DataFrame(supplement_guide)
df_meal = pd.DataFrame(meal_plan)
df_progress = pd.DataFrame(progress_journal)

# Save to Excel
file_path = "/mnt/data/60_Day_Glow_Up_Tracker.xlsx"
with pd.ExcelWriter(file_path) as writer:
    df_daily.to_excel(writer, sheet_name="Daily Habits", index=False)
    df_workout.to_excel(writer, sheet_name="Workout Plan", index=False)
    df_supplements.to_excel(writer, sheet_name="Supplement Guide", index=False)
    df_meal.to_excel(writer, sheet_name="Meal Plan", index=False)
    df_progress.to_excel(writer, sheet_name="Progress Journal", index=False)

file_path
