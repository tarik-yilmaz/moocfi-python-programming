# Write your solution here
from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthdate = datetime(year, month, day)

millenium_eve = datetime(1999, 12, 31)

difference = millenium_eve - birthdate

if birthdate > millenium_eve:
    print(f"You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")