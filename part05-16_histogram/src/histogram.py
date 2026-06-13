# Write your solution here
def histogram(word: str):
    if len(word) < 1:
        return
    
    histo_dictionary = {}

    index = 0

    while index < len(word):
        if word[index] not in histo_dictionary:
            histo_dictionary[word[index]] = []
            histo_dictionary[word[index]].append("*")
            index += 1
        else:
            histo_dictionary[word[index]].append("*")
            index += 1

    for key, value in histo_dictionary.items():
        print(f"{key} ", end="")
        for star in value:
            print(star, end="")
        print()


