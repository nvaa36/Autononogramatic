import sys
from reader import *

def main():
    (cols, rows, col_vals, row_vals) = read_nonogram("ex1.txt")
    solution = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row += [0]
        solution.append(row)
    print(cols)
    print(rows)
    print(col_vals)
    print(row_vals)
    print(solution)

    fill_max_lines(solution, cols, rows, col_vals, row_vals)
    print(solution)

    while not is_done(solution, rows, cols):
        i = 2

def is_done(solution, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] == 0:
                return False
    return True

# Fill in all of the rows and columns that contain the maximum value for the
# row/column
def fill_max_lines(solution, cols, rows, col_vals, row_vals):
    for i in range(rows):
        sum_vals = sum(row_vals[i])
        if (sum_vals + len(row_vals[i]) - 1) == cols:
            fill_row(solution, i, row_vals)

def fill_row(solution, row, row_vals):
    val_ind = 0
    row_val = row_vals[row]
    for col in range(len(solution[row])):
        if row_val[val_ind] == 0:
            solution[row][col] = 'X'
            val_ind += 1
        else:
            solution[row][col] = '@'
            row_val[val_ind] -= 1


if __name__ == "__main__":
    main()
