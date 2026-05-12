# Write your solution here

hourly = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday != "Sunday":
    sum = hourly * hours
    print(f"Daily wages: {sum} euros")

if weekday == "Sunday":
    sum = 2 * (hours * hourly)
    print(f"Daily wages: {sum } euros")