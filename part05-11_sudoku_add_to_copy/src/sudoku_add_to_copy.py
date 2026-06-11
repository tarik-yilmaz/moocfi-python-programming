# Write your solution here

def print_sudoku(sudoku: list):
    for row_index in range(len(sudoku)):
        row = sudoku[row_index]

        for col_index in range(len(row)):
            if col_index > 0 and col_index % 3 == 0:
                print(" ", end="")

            number = row[col_index]

            if number == 0:
                print("_", end=" ")
            else:
                print(number, end=" ")

        print()

        if (row_index + 1) % 3 == 0:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    new_sudoku = []
    
    for row in sudoku:
        new_sudoku.append(row[:])

    new_sudoku[row_no][column_no] = number
    
    return new_sudoku
