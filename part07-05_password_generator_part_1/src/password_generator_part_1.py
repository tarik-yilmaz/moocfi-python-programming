# Write your solution here
import string, random

def generate_password(length: int) -> str:
    letter_list = random.sample(string.ascii_lowercase, length)

    password = ""

    for character in letter_list:
        password += character

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))