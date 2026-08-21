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
    
    # Iterates over all the nine squares 
    # (why the fk does a negative index not cause an IndexError in python 😭) 
    # and then just subtracts the cell itself.

    for r in [row-1, row, row+1]:
        for c in [col-1, col, col+1]:
            try:
                if r >= 0 and c >= 0:
                    alive_count += grid[r][c]
            except IndexError:
                continue

    alive_count -= grid[row][col]

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
    
    # iterates over the whole grid and then applies rules using if statements.

    for r in range(0,rows):
        for c in range(0,cols):
            neighbors = count_neighbors(grid, r, c)
            if neighbors < 2:
                continue # cell is dead by default.
            if neighbors == 2:
                next_grid[r][c] = grid[r][c]
            if neighbors == 3: # when there are 3 neighbours then cell is alive next tick anyways.
                next_grid[r][c] = 1
            if neighbors > 3:
                continue # cell is dead by default.

    return next_grid
