# Write your solution here

def filter_solutions():

    with open("solutions.csv") as file:
        with open("correct.csv", "w") as correct_file:
            with open("incorrect.csv", "w") as incorrect_file:
                for line in file:
                    line = line.replace("\n", "")

                    parts = line.split(";")

                    name = parts[0]
                    is_equal = int(parts[2])

                    if '+' in parts[1]:
                        numbers = parts[1].split("+")
                        add1 = int(numbers[0])
                        add2 = int(numbers[1])

                        if add1 + add2 == is_equal:
                            correct_file.write(f"{name};{add1}+{add2};{is_equal}\n")
                        else:
                            incorrect_file.write(f"{name};{add1}+{add2};{is_equal}\n")

                    else:
                        numbers = parts[1].split("-")
                        sub1 = int(numbers[0])
                        sub2 = int(numbers[1])
                        
                        if sub1 - sub2 == is_equal:
                            correct_file.write(f"{name};{sub1}-{sub2};{is_equal}\n")
                        else:
                            incorrect_file.write(f"{name};{sub1}-{sub2};{is_equal}\n")

if __name__ == "__main__":
    filter_solutions()