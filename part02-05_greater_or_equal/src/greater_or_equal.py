# Write your solution here

first_number = int(input("Please type in first number: "))
second_number = int(input("Please type in another number: "))

if first_number > second_number:
    print(f"The greater number was: {first_number}")
elif second_number > first_number:
    print(f"The greater number was: {second_number}")
else:
    print("The numbers are equal!")