# Write your solution here

from datetime import datetime, timedelta
    
# Read inputs
filename =  input("Filename: ")
start_date = input("Starting date: ")
duration_days = int(input("How many days: "))

# Try converting date and return if wrong
try:
    start_date = datetime.strptime(start_date, "%d.%m.%Y")
except ValueError:
    print("Wrong date format!")


print("Please type in screen time in minutes on each day (TV computer mobile):")

# Create an empty list and variables for calculations
date_and_minutes = []
total_minutes = 0

current_date = start_date

for i in range(duration_days):
    date_string = current_date.strftime("%d.%m.%Y")
    minutes_to_add = input(f"Screen time {date_string}: ")

    parts = minutes_to_add.split()

    if len(parts) != 3:
        break
    
    tv = int(parts[0])
    computer = int(parts[1])
    mobile = int(parts[2])

    daily_total = tv + computer + mobile
    total_minutes += daily_total

    date_and_minutes.append((date_string, f"{tv}/{computer}/{mobile}"))
    
    current_date = current_date + timedelta(days=1)

# Calculate average
average_minutes = total_minutes /  duration_days

# Calculate end date
end_date = start_date + timedelta(days=duration_days - 1)

with open(filename, "w") as new_file:
    new_file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    new_file.write(f"Total minutes: {total_minutes}\n")
    new_file.write(f"Average minutes: {average_minutes}\n")

    for date, minutes in date_and_minutes:
        new_file.write(f"{date}: {minutes}\n")

print(f"Data stored in file {filename}")
