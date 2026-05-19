# Write your solution here

user_input = input("Please type in a string: ")

missing_stars = 20 - len(user_input)

print(f"{missing_stars * "*"}{user_input} ")