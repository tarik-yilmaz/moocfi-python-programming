# Write your solution here

def longest_series_of_neighbours(neighbours: list[int]) -> int:
    if len(neighbours) == 0:
        return 0
    
    current = 1
    longest = 1
    
    index = 0

    while index < len(neighbours):
        if neighbours[index] == neighbours[index - 1] + 1  or neighbours[index] == neighbours[index - 1] - 1:
            current += 1

            if current > longest:
                longest = current

        else:
            current = 1
        
        index += 1

    return longest