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
    """

    # Get the number of rows and columns in the current grid.
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Create a separate grid for the next generation.
    # Every cell starts as dead (0)

    # not modifying grid directly because neighbour counts must always be calculated using the original generation.
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Visit every cell in the current generation
    for row in range(rows):
        for col in range(cols):
            # Count the live cells among the 8 neighbouring positions
            live_neighbors = count_neighbors(grid, row, col)

            # If the current cell is alive
            if grid[row][col] == 1:
                # A live cell survives with exactly 2 or 3 live neighbours
                if live_neighbors in (2, 3):
                    new_grid[row][col] = 1

                # Otherwise it remains 0 (dies due to underpopulation or overpopulation)
            # If the current cell is dead
            else:
                # A dead cell becomes alive if it has exactly 3 live neighbours
                if live_neighbors == 3:
                    new_grid[row][col] = 1

                # Otherwise it remains 0.
    # Return the newly calculated generation.
    return new_grid



