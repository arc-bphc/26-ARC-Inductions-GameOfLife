import os
import time
import random
import sys
import shutil

try:
    from solver import compute_next_generation, count_neighbors
except ImportError:
    def compute_next_generation(grid):
        print("\033[91m[!] Error: Could not import from solver.py\033[0m")
        sys.exit(1)
    
    def count_neighbors(grid, row, col):
        return 0

if os.name == 'nt':
    import msvcrt
    def setup_terminal():
        return None
    def restore_terminal(settings):
        pass
    def check_input():
        if msvcrt.kbhit():
            try:
                return msvcrt.getch().decode('utf-8', 'ignore').lower()
            except:
                pass
        return None
else:
    import select
    import termios
    import tty
    def setup_terminal():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        return old_settings
    def restore_terminal(settings):
        if settings:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, settings)
    def check_input():
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return sys.stdin.read(1).lower()
        return None

COLOR_BORDER = '\033[38;5;51m'
COLOR_TITLE = '\033[1;38;5;226m'
COLOR_STATS = '\033[38;5;250m'
COLOR_DEAD = '\033[38;5;236m'
COLOR_MUTED = '\033[38;5;239m'
COLOR_PLAY = '\033[38;5;46m'
COLOR_PAUSE = '\033[38;5;196m'
RESET = '\033[0m'

CHAR_ALIVE = '██'
CHAR_DEAD = '··'

def clear_screen(first_frame=False):
    if first_frame:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        sys.stdout.write('\033[H')
        sys.stdout.flush()

def get_heatmap_color(grid, r, c):
    try:
        neighbors = count_neighbors(grid, r, c)
    except Exception:
        neighbors = 0 
        
    if neighbors <= 1:
        return '\033[38;5;33m'
    elif neighbors == 2:
        return '\033[38;5;46m'
    elif neighbors == 3:
        return '\033[38;5;51m'
    else:
        return '\033[38;5;196m'

def print_grid(grid, generation, seed_type, paused, first_frame=False):
    clear_screen(first_frame)
    
    term_cols, term_lines = shutil.get_terminal_size((80, 24))
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    box_width = cols * 2
    
    pad_left_str = " " * max(0, (term_cols - box_width - 2) // 2)
    pad_top_lines = max(0, (term_lines - (rows + 6)) // 2)
    
    output = []
    output.extend([""] * pad_top_lines)
    
    output.append(f"{pad_left_str}{COLOR_BORDER}╭{'─' * box_width}╮{RESET}")
    
    title = " ARC'S GAME OF RETARDATION "
    t_pad = (box_width - len(title)) // 2
    output.append(f"{pad_left_str}{COLOR_BORDER}│{' ' * t_pad}{COLOR_TITLE}{title}{COLOR_BORDER}{' ' * (box_width - len(title) - t_pad)}│{RESET}")
    
    status_text = "PAUSED " if paused else "PLAYING"
    stats_raw = f" Gen: {generation:05d} | State: {status_text} | Seed: {seed_type.upper()} "
    s_pad = (box_width - len(stats_raw)) // 2
    
    status_colored = f"{COLOR_PAUSE}PAUSED {COLOR_STATS}" if paused else f"{COLOR_PLAY}PLAYING{COLOR_STATS}"
    stats_colored = f" Gen: {generation:05d} | State: {status_colored} | Seed: {seed_type.upper()} "
    
    output.append(f"{pad_left_str}{COLOR_BORDER}│{COLOR_STATS}{' ' * s_pad}{stats_colored}{' ' * (box_width - len(stats_raw) - s_pad)}{COLOR_BORDER}│{RESET}")
    output.append(f"{pad_left_str}{COLOR_BORDER}├{'─' * box_width}┤{RESET}")
    
    for r, row in enumerate(grid):
        row_str = f"{pad_left_str}{COLOR_BORDER}│{RESET}"
        for c, cell in enumerate(row):
            if cell == 1:
                color = get_heatmap_color(grid, r, c)
                row_str += f"{color}{CHAR_ALIVE}{RESET}"
            else:
                row_str += f"{COLOR_DEAD}{CHAR_DEAD}{RESET}"
        row_str += f"{COLOR_BORDER}│{RESET}"
        output.append(row_str)
        
    output.append(f"{pad_left_str}{COLOR_BORDER}╰{'─' * box_width}╯{RESET}")
    
    instr = "Press [SPACE] to Play/Pause, [Q] to Quit"
    i_pad = " " * max(0, (term_cols - len(instr)) // 2)
    output.append(f"{i_pad}{COLOR_MUTED}{instr}{RESET}")
    
    sys.stdout.write("\n".join(output) + "\n")
    sys.stdout.flush()

def get_seed(seed_type='random', rows=20, cols=40):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    if seed_type == 'glider':
        grid[1][2] = 1
        grid[2][3] = 1
        grid[3][1] = 1
        grid[3][2] = 1
        grid[3][3] = 1
        
    elif seed_type == 'blinker':
        grid[5][5] = 1
        grid[5][6] = 1
        grid[5][7] = 1
        
    elif seed_type == 'pulsar':
        center_r, center_c = rows // 2, cols // 2
        for r, c in [(2,1), (3,1), (4,1), (1,2), (1,3), (1,4),
                     (2,6), (3,6), (4,6), (6,2), (6,3), (6,4)]:
            grid[center_r - r][center_c - c] = 1
            grid[center_r - r][center_c + c] = 1
            grid[center_r + r][center_c - c] = 1
            grid[center_r + r][center_c + c] = 1
            
    else:
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = random.choices([0, 1], weights=[80, 20])[0]
                
    return grid

def main():
    ROWS = 20
    COLS = 35
    TICK_SPEED = 0.1
    #---------------------------- 
    SEED_TYPE = 'random' #glider/blinker/pulsar (default: random)
    #---------------------------- 
    
    grid = get_seed(SEED_TYPE, ROWS, COLS)
    generation = 0
    
    last_term_size = shutil.get_terminal_size((80, 24))
    first_frame = True
    paused = True
    last_tick_time = time.time()
    
    term_settings = setup_terminal()
    
    try:
        while True:
            current_term_size = shutil.get_terminal_size((80, 24))
            if current_term_size != last_term_size:
                first_frame = True
                last_term_size = current_term_size

            key = check_input()
            if key == ' ':
                paused = not paused
            elif key == 'q' or key == '\x03':
                break

            print_grid(grid, generation, SEED_TYPE, paused, first_frame)
            first_frame = False
            
            now = time.time()
            if not paused and (now - last_tick_time) >= TICK_SPEED:
                grid = compute_next_generation(grid)
                generation += 1
                last_tick_time = now
                
            time.sleep(0.03)
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n\033[91m[!] An error occurred during simulation:\033[0m")
        print(f"{e}")
        print("\nCheck your compute_next_generation logic in solver.py!")
    finally:
        restore_terminal(term_settings)
        print(f"\n{COLOR_BORDER}Simulation stopped.{RESET}\n")

if __name__ == '__main__':
    main()