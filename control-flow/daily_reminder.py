
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = "is a high priority task"
    case "medium":
        reminder = "is a medium priority task"
    case "low":
        reminder = "is a low priority task"
    case _:
        reminder = "has an unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
print(f"{task}", reminder)
