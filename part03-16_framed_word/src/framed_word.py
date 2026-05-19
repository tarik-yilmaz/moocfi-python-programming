# Write your solution here

user_input = input("Word: ")

width = 30
star = "*"

print(star * width)

spaces = width - len(user_input) - 2

left_spaces = spaces // 2
right_spaces = spaces - left_spaces

middle_part = star + " " * left_spaces + user_input + " " * right_spaces + star

print(middle_part)
print(star * width)