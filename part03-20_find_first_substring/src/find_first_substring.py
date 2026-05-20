# Write your solution here

input_string = input("Please type in a word: ")
character = input("Please type in a character: ")

if character in input_string:
    index = input_string.find(character)
    next = index + 3

    if next <= len(input_string):
        print(input_string[index:next])