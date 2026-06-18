# write your solution here

def matrix_sum() -> int:
    sum_all = 0

    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            number_list = line.split(",")
            
            for num in number_list:
                sum_all += int(num)
            
    return sum_all


def matrix_max() -> int:
    max_number = 0

    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            number_list = line.split(",")

            for num in number_list:
                if int(num) > max_number:
                    max_number = int(num)
    
    return max_number

def row_sums() -> list:
    sum_of_row = 0
    list_of_row_sums = []

    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            row_list = line.split(",")

            for num in row_list:
                sum_of_row += int(num)
            
            list_of_row_sums.append(sum_of_row)
            sum_of_row = 0

    return list_of_row_sums

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())