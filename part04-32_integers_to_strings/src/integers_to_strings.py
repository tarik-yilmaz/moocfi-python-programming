# Write your solution here

def formatted(numbers: list[float]) -> list[str]:
    new_list = []

    for num in numbers:
        new_list.append(f"{num:.2f}")

    return new_list