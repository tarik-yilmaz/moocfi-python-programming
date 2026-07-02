# Write your solution here
import string, random

def generate_strong_password(length: int, number_flag: bool, punctuation_flag: bool) -> str:

    password = ""
    possible_characters = string.ascii_lowercase
    special_characters = "!?=+-()#"

    password += random.choice(string.ascii_lowercase)

    if number_flag == True:
        password += random.choice(string.digits)
        possible_characters += string.digits

    if punctuation_flag == True:
        password += random.choice(special_characters)
        possible_characters += special_characters

    while len(password) < length:
        password += random.choice(possible_characters)

    password_list = list(password)

    random.shuffle(password_list)

    password = ""

    for character in password_list:
        password += character


    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))

    for i in range(3):
        print(generate_strong_password(5, False, False))