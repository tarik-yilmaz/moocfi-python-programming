# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int) -> dict:
    word_list = []
    with open(f"src/{filename}") as file:
        for line in file:
            
            for character in string.punctuation:
                line = line.replace(character, "")
            word_list += line.split()

    return {word : word_list.count(word) for word in word_list if word_list.count(word) >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))