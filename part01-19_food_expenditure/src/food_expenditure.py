# Write your solution here
times_a_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_per_lunch = float(input("The price of a typical student lunch? " ))
weekly_expenses = float(input("How much money do you spend on groceries in a week? "))

daily = (weekly_expenses  + times_a_week * price_per_lunch) / 7
weekly = weekly_expenses + price_per_lunch * times_a_week

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")