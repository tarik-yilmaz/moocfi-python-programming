# Write your solution here

def sudoku_grid_correct(sudoku: list) -> bool:
    for row_no in range(9):
         if not row_correct(sudoku, row_no):
              return False
         
    for column_no in range(9):
         if not column_correct(sudoku, column_no):
              return False
         
    for row_no in range(0, 9, 3):
         for column_no in range(0, 9, 3):
              if not block_correct(sudoku, row_no, column_no):
                   return False
              
    return True


def row_correct(sudoku: list, row_no: int) -> bool:
    check_list = []
    

    for number in sudoku[row_no]:
            if number > 0 and number in check_list:
                return False
            else:
                check_list.append(number)
    
    return True


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


def column_correct(sudoku: list, column_no: int) -> bool:
    check_list = []

    for row  in sudoku:
        number = row[column_no]

        if number > 0 and number in check_list:
            return False
        else:
            check_list.append(number)

    return True
