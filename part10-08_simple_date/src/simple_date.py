# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        if day > 0:
            self.__day = day
        if month > 0 and month <= 12:
            self.__month = month
        if year > 0:
            self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __lt__(self, another):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year:
            if self.__month < another.__month:
                return True
            elif self.__month == another.__month:
                if self.__day < another.__day:
                    return True

        return False

    def __gt__(self, another):
        if self.__year > another.__year:
            return True
        elif self.__year == another.__year:
            if self.__month > another.__month:
                return True
            elif self.__month == another.__month:
                if self.__day > another.__day:
                    return True
        return False

    def __eq__(self, another):
        if self.__day == another.__day and self.__month == another.__month and self.__year == another.__year:
            return True
        else:
            return False

    def __ne__(self, another):
        if self.__day == another.__day and self.__month == another.__month and self.__year == another.__year:
            return False
        else:
            return True

    def __add__(self, amount):
        day = self.__day
        month = self.__month
        year = self.__year

        total_days = amount

        while total_days > 0:
            total_days -= 1
            day += 1
            if day > 30:
                month += 1
                day = 1
                if month > 12:
                    year += 1
                    month = 1
                    
        return SimpleDate(day, month, year)

    def __sub__(self, another):
        days = self.__day
        days += self.__month * 30
        days += self.__year * 360

        sub_days = another.__day
        sub_days += another.__month * 30
        sub_days += another.__year * 360

        result  = days - sub_days

        if result < 0:
            return result * (-1)
        else:
            return result
        
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print("Part 1: Comparisons")
    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)
    print("-------------------------------")

    print("Part 2: Increment")
    d3 = d1 + 3
    d4 = d2 + 400
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print("-------------------------------")

    print("Part 3: Difference")
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)
    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
    print("-------------------------------")
