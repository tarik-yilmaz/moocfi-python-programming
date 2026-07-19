# Write your solution here

from difflib import get_close_matches

user_text = input("write text: ")
words = []

with open("src/wordlist.txt") as wordlist:
    for line in wordlist:
        line = line.replace("\n", "").lower()

        words.append(line)

parts = user_text.split(" ")

suggestion_list = []

for word in parts:
    if word.lower() not in words:
        print(f"*{word}* ", end="")
        suggestion_list.append(word)
    else:
        print(f"{word} ", end ="")

print("\nsuggestions:")

for word in suggestion_list:
    suggestions = get_close_matches(word, words)

    print(f"{word}: ", end="")

    length = len(suggestions)

    for i in range(len(suggestions)):
        print(suggestions[i], end="")

        if i < len(suggestions) - 1:
            print(", ", end="")
            
    print()
