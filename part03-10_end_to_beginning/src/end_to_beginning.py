# Write your solution here

user_input = input("Please type in a string: ")
index  = len(user_input) - 1

while index >= 0:
    print(user_input[index])
    index -= 1
