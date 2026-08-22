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
    # directions to move from the particular cell to check if its a corner or an edge
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    for dir_row, dir_col in directions:
        # move to the neighbouring cell 
        curr_row = row + dir_row 
        curr_col = col + dir_col 

        # check if its still in the grid
        if (0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])):
            alive_count += grid[curr_row][curr_col] # works as it increments 1 when alive

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
    
   
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    return next_grid




