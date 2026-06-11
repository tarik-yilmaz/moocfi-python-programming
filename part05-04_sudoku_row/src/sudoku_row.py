# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
    check_list = []
    

    for number in sudoku[row_no]:
            if number > 0 and number in check_list:
                return False
            else:
                check_list.append(number)
    
    return True