# WRITE YOUR SOLUTION HERE:

class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight


    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.box = []
        self.combined_weight = 0

    def add_present(self, present: Present):
        self.box.append(present)
        self.combined_weight += present.weight

    def total_weight(self):
        return self.combined_weight


if __name__ == "__main__":
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())