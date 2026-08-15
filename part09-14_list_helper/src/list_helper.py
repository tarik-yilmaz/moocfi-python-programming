# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_common = 0
        highest_count = 0

        # Set helps to reduce the number of comparisons by only comparing unique values
        for item in set(my_list):
            count = my_list.count(item)

            if count > highest_count:
                highest_count = count
                most_common = item

        return most_common

        # Alternative elegant solution (stackoverflow)
        return max(set(my_list), key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list):
        doubles = 0

        for item in set(my_list):

            count = my_list.count(item)

            if count >= 2:
                doubles += 1

        return doubles

if __name__ == "__main__": 
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))