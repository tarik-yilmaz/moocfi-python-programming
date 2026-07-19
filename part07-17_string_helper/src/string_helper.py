# Write your solution here
from string import ascii_letters, digits

def change_case(orig_string: str) -> str:
    new_string = ""

    for character in orig_string:
        if character.islower():
            new_string += character.upper()
        else:
            new_string += character.lower()
    
    return new_string

def split_in_half(orig_string: str) -> tuple:
    middle = len(orig_string) // 2
    first_part = ""
    second_part = ""

    for i in range(len(orig_string)):
        if i < middle:
            first_part += orig_string[i]
        else:
            second_part += orig_string[i]
    
    return (first_part, second_part)

def remove_special_characters(orig_string: str) -> str:
    new_string = ""
    allowed = ascii_letters + digits + ' '
    
    for character in orig_string:
        if character in allowed:
            new_string += character

    return new_string


if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    m3 = remove_special_characters("Thi§ is a test test")
    print(m2)
    print(m3)