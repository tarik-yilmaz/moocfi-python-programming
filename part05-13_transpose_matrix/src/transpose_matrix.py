# Write your solution here

def transpose(matrix: list):
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
