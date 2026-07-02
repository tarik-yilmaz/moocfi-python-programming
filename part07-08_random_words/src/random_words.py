# Write your solution here
import random

def words(n: int, beginning: str) -> list:
    if n < 0:
        raise ValueError("Number of words cannot be negative!")
    
    word_list = []
    
    try:
        with open ("src/words.txt") as file:
            for line in file:
                line = line.replace("\n", "")

                if line.startswith(beginning):
                    word_list.append(line)
    except FileNotFoundError:
        print("File words.txt doesn't exist!") 
    
    if n > len(word_list):
        raise ValueError("Number of words exceeding list!")

    return random.sample(word_list, n)

if __name__ == "__main__":
    # word_list = words(1000, "car")
    
    word_list = words(10, "car")
    for word in word_list:
        print(word)