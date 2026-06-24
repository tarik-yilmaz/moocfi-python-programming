# write your solution here

text = input("Write text: ").strip()

parts = text.split(" ")

word_list = []
checked_list = []

with open(f"src/wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")

        word_list.append(line.lower())


for word in parts:
    if word.lower() in word_list:
        checked_list.append(word)
    else:
        checked_list.append(f"*{word}*")

for word in checked_list:
    print(word, end=" ")

