# Write your solution here

def distinct_numbers(my_list: list[int]) -> list[int]:
    new_list = []

    for i in my_list:
        if i not in new_list:
            new_list.append(i)

    return sorted(new_list)
