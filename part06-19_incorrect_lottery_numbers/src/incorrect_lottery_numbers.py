# Write your solution here

def filter_incorrect():
    try:
        with open("lottery_numbers.csv") as file:
            with open("correct_numbers.csv", "w") as new_file:

                for line in file:
                    line = line.replace("\n", "")
                    valid = True

                    parts = line.split(";")

                    if len(parts) != 2:
                        valid = False
                    else:
                        week_part = parts[0]
                        numbers_part = parts[1]

                        week_parts = week_part.split(" ")

                        if len(week_parts) != 2:
                            valid = False
                        else:
                            try:
                                week_number = int(week_parts[1])
                            except ValueError:
                                valid = False

                        numbers_as_strings = numbers_part.split(",")
                        number_check_list = []

                        if len(numbers_as_strings) != 7:
                            valid = False

                        for num in numbers_as_strings:
                            try:
                                num = int(num)
                            except ValueError:
                                valid = False
                                continue

                            if num < 1 or num > 39:
                                valid = False

                            if num in number_check_list:
                                valid = False

                            number_check_list.append(num)

                    if valid:
                        new_file.write(line + "\n")

    except FileNotFoundError:
        print("File does not exist!")