import math


students = int(input("How many students are going? "))
teachers = int(input("How many teachers are going? "))
richKids = int(input("How many students brought their own skates? "))

busPrice = 200 * (math.ceil((students + teachers) / 50))
lunchPrice = students * 5 + teachers * 7
skatePrice = 4 * students - richKids * 4
totalPrice = busPrice + lunchPrice + skatePrice

print(f"Bus cost: {busPrice}")
print(f"Lunch cost: {lunchPrice}")
print(f"Rental cost: {skatePrice}")
print(f"Total cost: {totalPrice}")

