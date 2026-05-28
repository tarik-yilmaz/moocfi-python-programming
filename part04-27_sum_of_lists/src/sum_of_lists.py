# Write your solution here

def list_sum(first_list: list, second_list: list) -> list:
    new_list = []
    index = 0

    while index < len(first_list):
        new_list.append(first_list[index] + second_list[index])
        index += 1

    return new_list
