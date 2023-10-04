initHours = int(input("Enter time in hours: "))
weeks = initHours // 168
initHours -= weeks * 168
days = initHours // 24
hours = initHours % 24
print(f"{weeks} weeks, {days} days, and {hours} hours")

