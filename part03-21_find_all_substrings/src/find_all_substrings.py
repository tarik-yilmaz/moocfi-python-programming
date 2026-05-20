# Write your solution here

input_string = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    part = input_string.find(character)
    
    if part == -1:
        break

    end = part + 3

    if end <= len(input_string):
        print(input_string[part:end])

    input_string = input_string[part + 1:]