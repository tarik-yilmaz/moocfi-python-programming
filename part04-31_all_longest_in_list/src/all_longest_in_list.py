# Write your solution here

def all_the_longest(my_list: list[str]) -> list[str]:
    new_list = []
    longest_word = ""

    for i in my_list:
        if len(i) >= len(longest_word):
            longest_word = i
    
    for i in my_list:
        if len(i) >= len(longest_word):
            new_list.append(i)

    return new_list
