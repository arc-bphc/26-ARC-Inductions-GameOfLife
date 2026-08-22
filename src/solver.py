#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:

            if row_offset == 0 and col_offset == 0:
                continue

            new_row = row + row_offset
            new_col = col + col_offset

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == 1:
                    alive_count += 1

    return alive_count




#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # TODO: Iterate through every cell in the `grid`.
    # TODO: Use your `count_neighbors` function to find out how many neighbors it has.
    # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.
def compute_next_generation(grid): 
 
    rows = len(grid) 
    cols = len(grid[0]) if rows > 0 else 0 
 
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)] 
 
    for row in range(rows): 
        for col in range(cols): 
 
            neighbors = count_neighbors(grid, row, col) 
 
            if grid[row][col] == 1: 
 
                if neighbors == 2 or neighbors == 3: 
                    next_grid[row][col] = 1 
 
            else: 
 
                if neighbors == 3: 
                    next_grid[row][col] = 1 
 
    return next_grid