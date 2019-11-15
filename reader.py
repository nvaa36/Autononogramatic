def read_nonogram(file_name):
    f = open(file_name, "r")
    cols = (int)(f.readline())
    rows = (int)(f.readline())
    row_vals = []
    col_vals = []

    for i in range(cols):
        col_vals.append(list(map(int, f.readline().split())))

    for i in range(rows):
        row_vals.append(list(map(int, f.readline().split())))

    return (cols, rows, col_vals, row_vals)
