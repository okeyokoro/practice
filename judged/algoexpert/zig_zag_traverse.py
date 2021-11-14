""" category: arrays """

def zigzagTraverse(array):
    
    max_row = len(array) - 1
    max_col = len(array[0]) - 1
    
    first_column = lambda col: col == 0
    first_row = lambda row: row == 0
    last_row = lambda row: row == max_row
    last_col = lambda col: col == max_col
    last_element = lambda index: index.row == max_row and index.col == max_col
    
    class Index2D:
        def __init__(self, row, col):
            if 0 <= row <= max_row and 0 <= col <= max_col:
                self.row = row
                self.col = col
            else:
                print(f"row: {row}, col: {col}")
                raise Exception(f"row: {row}, col: {col}")
    
    current_idx = Index2D(row=0, col=0)
    
    go_down = lambda current_idx: Index2D(row=current_idx.row+1,  col=current_idx.col)
    go_right = lambda current_idx: Index2D(row=current_idx.row,  col=current_idx.col+1)
    zig_zag_up = lambda current_idx: Index2D(row=current_idx.row-1,  col=current_idx.col+1)
    zig_zag_down = lambda current_idx: Index2D(row=current_idx.row+1,  col=current_idx.col-1)
    
    zig_zaging_direction = ""
    
    solution = []

    while True:
        solution.append( array[current_idx.row][current_idx.col] )
        print(solution)
        
        if last_element(current_idx):
            return solution
        
        if first_column(current_idx.col) and zig_zaging_direction == "up":
            try:
                current_idx = zig_zag_up(current_idx)
            except:
                current_idx = go_down(current_idx)
            continue

        if first_row(current_idx.row) and zig_zaging_direction == "down":
            try:
                current_idx = zig_zag_down(current_idx)
            except:
                current_idx = go_right(current_idx)
            continue
    
        if first_column(current_idx.col):
            try:
                current_idx = go_down(current_idx)
            except:
                current_idx = go_right(current_idx)
            zig_zaging_direction = "up"
            continue
        
        if first_row(current_idx.row):
            try:
                current_idx = go_right(current_idx)
            except:
                current_idx = go_down(current_idx)
            zig_zaging_direction = "down"
            continue
        
        if last_row(current_idx.row) and zig_zaging_direction == "down":
            current_idx = go_right(current_idx)
            zig_zaging_direction = "up"
            continue

        if last_col(current_idx.col) and zig_zaging_direction == "up":
            current_idx = go_down(current_idx)
            zig_zaging_direction = "down"
            continue
        
        if zig_zaging_direction == "up":
            current_idx = zig_zag_up(current_idx)
            continue

        if zig_zaging_direction == "down":
            current_idx = zig_zag_down(current_idx)
            continue
