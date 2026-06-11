# Write your solution here

def block_correct(sudoku: list, row_no: int, col_no: int) -> bool:
    check_list = []

    for row in range(row_no, row_no + 3):
        for col in  range(col_no, col_no + 3):
            number = sudoku[row][col]

            if number > 0 and number in check_list:
                    return False
            else:
                 check_list.append(number)
    
    return True

        