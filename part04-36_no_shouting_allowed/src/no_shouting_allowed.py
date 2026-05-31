# Write your solution here

def no_shouting(words: list[str]) -> list[str]:
    new_list = []

    for word in words:
        if word.isupper() == False:
            new_list.append(word)
    
    return new_list