# Write your solution here

def times_ten(start_index: int, end_index: int) -> dict:
    my_dictionary = {}

    while start_index <= end_index:
        my_dictionary[start_index] = start_index * 10
        start_index += 1

    return my_dictionary
    