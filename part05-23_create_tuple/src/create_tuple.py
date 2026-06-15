# Write your solution here

def create_tuple(x: int, y: int, z: int) -> tuple:
    smallest = x
    greatest = x
    sum = 0

    numbers = (x, y, z)

    for n in numbers:
        if n < smallest:
            smallest = n

        if n > greatest:
            greatest = n

        sum += n
        
    return (smallest, greatest, sum)
