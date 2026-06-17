# write your solution here

def largest():

    with open("src/numbers.txt") as new_file:
        initial_number = new_file.readline(0)

        for line in new_file:
            if initial_number < line:
                initial_number = line

    return int(initial_number)


if __name__ == "__main__":
    largest_number = largest()
    print(largest_number, end="")
