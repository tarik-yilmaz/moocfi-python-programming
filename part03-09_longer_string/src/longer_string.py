# Write your solution here

first_string = input("Please type in string 1: ")
second_string = input("Please type in string 2: ")

if len(first_string) > len(second_string):
    print(f"{first_string} is longer")
elif len(first_string) == len(second_string):
    print("The strings are equally long")
else:
    print(f"{second_string} is longer")