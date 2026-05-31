# Write your solution here

def everything_reversed(words: list[str]) -> list[str]:
    reversed_list = []

    for word in words:
        reversed_list.append(word[::-1])
    
    return reversed_list[::-1]