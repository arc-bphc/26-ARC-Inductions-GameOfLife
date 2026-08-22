#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):   
    alive_count = 0
    r=len(grid)
    c=len(grid[0])
    for row_counter in[-1,0,1]:
        for col_counter in[-1,0,1]:
            if row_counter==0 and col_counter==0:
                continue
        n_row=row+row_counter
        n_col=col+col_counter
        if 0<=n_row<r and 0<=n_col<c:
             if grid[n_row][n_col]==1:
                 alive_count=alive_count+1
    return alive_count
#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            alive_neighbors = count_neighbors(grid, row, col)
            if grid[row][col]==1:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    next_grid[row][col] = 1
            else:
                if alive_neighbors == 3:
                    next_grid[row][col] = 1
    return next_grid