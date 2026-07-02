# Write your solution here
from fractions import Fraction

def fractionate(amount: int) -> list:
    new_list = []

    times = amount
    while times > 0:
        new_list.append(Fraction(1, amount))
        times -= 1
    
    return new_list


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))