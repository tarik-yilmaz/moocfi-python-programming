# Write your solution here
def length_of_longest(my_list: list[str]) -> int:

    longest = ""

    for i in my_list:
        if len(i) > len(longest):
            longest = i
        
    return len(longest)
