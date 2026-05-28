# Write your solution here
# Note, that at this time the main program should not be written inside

def palindromes(word: str) -> bool:
    reversed_string = ""
    length = len(word) - 1

    while length >= 0:
        reversed_string += word[length]
        length -= 1

    if word == reversed_string:
        return True
    else:
        return False


while True:
    word = input("Please type in a palindrome: ")

    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

        