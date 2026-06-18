# write your solution here

def read_matrix():
    matrix_list = []

    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            number_list = line.split(",")

            row_list = []

            for num in number_list:
                row_list.append(int(num))

            matrix_list.append(row_list)

    return matrix_list       

def matrix_sum() -> int:
    sum_all = 0

    matrix = read_matrix()

    for row in matrix:
        for num in row:
            sum_all += num

    return sum_all

def matrix_max() -> int:

    matrix = read_matrix()
    max_number = matrix[0][0]

    for row in matrix:
        for num in row:
            if num > max_number:
                max_number = num

    return max_number

def row_sums() -> list:
    list_of_row_sums = []

    matrix = read_matrix()

    for row in matrix:
        sum_of_row = 0

        for num in row:
            sum_of_row += num
            
        list_of_row_sums.append(sum_of_row)
    
    return list_of_row_sums

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())