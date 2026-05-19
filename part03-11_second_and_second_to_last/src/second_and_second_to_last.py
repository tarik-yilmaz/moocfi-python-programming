# Write your solution here

user_input = input("Please type in a string: ")
second_character = user_input[1]
second_to_last_character = user_input[-2]

if second_character == second_to_last_character:
    print(f"The second and the second to last characters are {second_character}")
else:
    print("The second and the second to last characters are different")