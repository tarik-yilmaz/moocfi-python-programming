# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum_of_numbers = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1
        self.sum_of_numbers += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.sum_of_numbers

    def average(self):
        if self.count > 0:
            return self.sum_of_numbers / self.count

        return 0

def main():
    all_numbers = NumberStats()
    even_numbers = NumberStats()
    odd_numbers = NumberStats()

    while True:
        user_number = int(input("Please type in integer numbers: "))

        if user_number == -1:
            break

        if user_number % 2 == 0:
            even_numbers.add_number(user_number)
        else:
            odd_numbers.add_number(user_number)

        all_numbers.add_number(user_number)

    print(f"Sum of numbers: {all_numbers.get_sum()}")
    print(f"Mean of numbers: {all_numbers.average()}")
    print(f"Sum of even numbers: {even_numbers.get_sum()}")
    print(f"Sum of odd numbers: {odd_numbers.get_sum()}")

main()
