# Write your solution here

def column_correct(sudoku: list, column_no: int) -> bool:
    check_list = []

    for row  in sudoku:
        number = row[column_no]

        if number > 0 and number in check_list:
            return False
        else:
            check_list.append(number)

    return True
