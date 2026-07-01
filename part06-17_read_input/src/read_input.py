# Write your solution here

def read_input(text: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            number = int(input(text))

            if number >= lower_bound and number  <= upper_bound:
                return number
            else:
                print(f"You must type in an integer between {lower_bound} and {upper_bound}")
        except ValueError:
            print(f"You must type in an integer between {lower_bound} and {upper_bound}")
