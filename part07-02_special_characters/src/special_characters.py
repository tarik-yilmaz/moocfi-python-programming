# Write your solution here
import string

def separate_characters(my_string: str) -> tuple:
    upper_and_lower = ""
    punctuations = ""
    other_characters = ""

    for character in my_string:
        if character in string.ascii_letters:
            upper_and_lower += character
        elif character in string.punctuation:
            punctuations += character
        else:
            other_characters += character

    return (upper_and_lower, punctuations, other_characters)
