from graphics import Window
from maze import Maze

def main():
    MAX_CANVAS_WIDTH = 800
    MAX_CANVAS_HEIGHT = 600
    MARGIN = 24   
    is_first_run = True                           

    while True:
        if is_first_run:
            print_intro()

        try:
            cols = int(input("\nColumns: "))
            rows = int(input("Rows: "))
        except ValueError:
            print("Error: Please enter valid integers.\n")
            continue

        cell_width = MAX_CANVAS_WIDTH // cols
        cell_height = MAX_CANVAS_HEIGHT // rows
        CELL = min(cell_width, cell_height)

        board_w = (cols * CELL) + (MARGIN * 2)
        board_h = (rows * CELL) + (MARGIN * 2)
        win = Window(board_w, board_h)       

        maze = Maze(MARGIN, MARGIN, rows, cols, CELL, CELL, win)
        maze.solve()

        win.wait_for_close()  
        
        cont = input("\nGenerate another maze? (Y/N): ")
        if cont.strip().lower() == "n":
            print_closing()
            break
        is_first_run = False
        
def print_intro():
    print("\n" + "=" * 60)
    print("MAZE GENERATOR & SOLVER".center(60))
    print("=" * 60)
    print("""
Enter the dimensions of the maze below.

Tips:
    - Recommended max size: 32 x 32
    - After solving, close the window to continue""")

def print_closing():
    print("\n" + "-" * 60)
    print("Closing program. Thanks for using the Maze Generator!".center(60))
    print("-" * 60 + "\n")

if __name__ == "__main__":
    main()