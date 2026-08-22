# ---------------------------- TASK 1 ----------------------------
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

    # TODO: Implement your neighbor-counting logic here!

    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # a list of 2d transforms to get from the cell to its 8 neighbours in [x, y] format
    # grid[0][0] represents top left
    # starting from top left, proceeding clockwise
    transforms = [
        (-1, -1),
        (-1,  0),
        (-1,  1),
        ( 0,  1),
        ( 1,  1),
        ( 1,  0),
        ( 1, -1),
        ( 0, -1),
    ]

    for dr, dc in transforms:
        nb_row = row + dr
        nb_col = col + dc
        if 0 <= nb_row < num_rows and 0 <= nb_col < num_cols:
            if grid[nb_row][nb_col] == 1:
                alive_count += 1

    return alive_count


# ---------------------------- TASK 2 ----------------------------
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

    for r in range(rows):
        for c in range(cols):
            alive_count = count_neighbors(grid, r, c)
            if alive_count < 2: # rule 1: underpopulation - live cell dies, dead cell stays dead
                next_grid[r][c] = 0
            elif alive_count == 3: # rule 4: reproduction - live cell survives, dead cell becomes live
                next_grid[r][c] = 1
            elif alive_count > 3: # rule 3: overpopulation - live cell dies, dead cell stays dead
                next_grid[r][c] = 0
            elif alive_count == 2 and grid[r][c] == 1: # rule 2: survival - live cell survives, dead cell stays dead
                next_grid[r][c] = 1

    return next_grid
