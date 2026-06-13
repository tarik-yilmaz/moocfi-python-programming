# Write your solution here

def factorials(n: int) -> dict:
    my_dictionary = {}
    
    if n < 0:
        return my_dictionary

    factor = 1
    sum = 1

    while factor <= n:
        my_dictionary[factor] = sum
        factor += 1
        sum *= factor

    return my_dictionary
