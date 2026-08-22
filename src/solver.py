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

    #finding the boundaries
    rows=len(grid)
    cols=len(grid[0]) if rows>0 else 0

    #for checking all neighbours
    for r in [-1,0,1]:
        for c in [-1,0,1]:
            if r==c==0:  #to skip the same cell
                continue

            #finding coordinates of the neighbours
            neighbour_row=row+r
            neighbour_col=col+c

            if (0<=neighbour_row<rows) and (0<=neighbour_col<cols):    #checking the boundary condition
                if grid[neighbour_row][neighbour_col]==1:      #checking if neighbour is alive
                    alive_count+=1

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
    
    #iterating through all cells
    for r in range(rows):
        for c in range(cols):
            n=count_neighbors(grid,r,c)  #finding count of alive neighbours

            #checking the rules
            if grid[r][c] and n in [2,3]:   
                next_grid[r][c]=1
            elif not(grid[r][c]) and n==3:
                next_grid[r][c]=1

    return next_grid