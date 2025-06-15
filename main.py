from graphics import Window
from maze import Maze

def main():
    MAX_CANVAS_WIDTH = 800
    MAX_CANVAS_HEIGHT = 600
    MARGIN = 24   
    is_first_run = True                           

    while True:
        if is_first_run:
            print(
"""
Please enter the dimensions of the maze below. 
-   Recommended maximum value for columns and rows is 32.
-   After the maze is solved, you will need to close the window for the program to continue to run.""")

        cols = int(input("\nColumns: "))
        rows = int(input("Rows: "))

        cell_width = MAX_CANVAS_WIDTH // cols
        cell_height = MAX_CANVAS_HEIGHT // rows
        CELL = min(cell_width, cell_height)

        board_w = (cols * CELL) + (MARGIN * 2)
        board_h = (rows * CELL) + (MARGIN * 2)
        win  = Window(board_w, board_h)       

        maze = Maze(MARGIN, MARGIN, rows, cols, CELL, CELL, win)
        maze.solve()

        win.wait_for_close()  
        
        cont = input("\nWant another one? (Y/N) ")
        if cont.lower() == "n":
            print("\nClosing program\n")
            break
        is_first_run = False
        

if __name__ == "__main__":
    main()