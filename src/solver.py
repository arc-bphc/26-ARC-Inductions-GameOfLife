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
    
    # Implementing my neighbor-counting logic here!
    
    # get total grid dimensions
    total_rows = len(grid)
    total_columns = len(grid[0]) if total_rows > 0 else 0
    
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            
            if not (total_rows > row >= 0 and total_columns > col >= 0): # skips if it is outside boundaries
                continue
            
            if not r == row and c == col: # skip center cell 
                continue
            if grid [r][c]:
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

    return next_grid