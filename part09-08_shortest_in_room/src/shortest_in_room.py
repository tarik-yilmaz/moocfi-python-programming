# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.combined_height = 0
        self.person_count = 0

    def add(self, person: Person):
        self.persons.append(person)
        self.combined_height += person.height
        self.person_count += 1

    def is_empty(self):
        return self.person_count <= 0

    def print_contents(self):
        print(f"There are {self.person_count} persons in the room, and their combined height is {self.combined_height} cm")
        if self.person_count > 0:
            for person in self.persons:
                    print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None

        shortest_person = self.persons[0]

        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person

        return shortest_person

    def remove_shortest(self):
        if self.is_empty():
            return None

        shortest_person = self.shortest()

        self.persons.remove(shortest_person)
        self.person_count -= 1
        self.combined_height -= shortest_person.height

        return shortest_person

if __name__ == "__main__":
    # Part 1
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    # Part 2
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    # Part 3
    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()