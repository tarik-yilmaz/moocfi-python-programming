# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, _euros: int, _cents: int):
        self.__euros = _euros
        self.__cents = _cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        else:
            return False

    def __lt__(self, another):
        if self.__euros < another.__euros:
            return True
        elif self.__euros == another.__euros and self.__cents < another.__cents:
            return True
        else:
            return False

    def __gt__(self, another):
        if self.__euros > another.__euros:
            return True
        elif self.__euros == another.__euros and self.__cents > another.__cents:
            return True
        else:
            return False
        

    def __ne__(self, another):
        if self.__euros != another.__euros or self.__cents !=  another.__cents:
            return True
        else:
            return False

    def __add__(self, another):
        total_cents = self.__euros * 100 + self.__cents + another.__euros * 100 + another.__cents

        euros = total_cents // 100
        cents = total_cents % 100

        return Money(euros, cents)

    def __sub__(self, another):
        self_cents = self.__euros * 100 + self.__cents
        another_cents = another.__euros * 100 + another.__cents

        difference = self_cents - another_cents

        if difference < 0:
            raise ValueError("a negative result is not allowed")

        euros = difference // 100
        cents = difference % 100

        return Money(euros, cents)

if __name__ == "__main__":
    # Part 1
    print("Part 1: Fix the string representation")
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print("----------------------")

    print("Part 2: Equal amounts")
    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
    print("----------------------")

    print("Part 3: Other comparison operators")
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    print("----------------------")

    print("Part 4: Addition and subtraction")
    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
    print("----------------------")

    print("Part 5: The value must not be directly accessible")
    print(e1)
    e1.euros = 1000
    print(e1)
    print("----------------------")