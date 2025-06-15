from graphics import Window
from maze import Maze

def main():
    MAX_CANVAS_WIDTH = 800
    MAX_CANVAS_HEIGHT = 600
    MARGIN = 24                              

    while True:
        print("Please enter the dimensions of the maze below: (recommended max is 32x32)")
        cols = int(input("Columns "))
        rows = int(input("Rows "))

        cell_width = MAX_CANVAS_WIDTH // cols
        cell_height = MAX_CANVAS_HEIGHT // rows
        CELL = min(cell_width, cell_height)

        board_w = (cols * CELL) + (MARGIN * 2)
        board_h = (rows * CELL) + (MARGIN * 2)
        win  = Window(board_w, board_h)       

        maze = Maze(MARGIN, MARGIN, rows, cols, CELL, CELL, win)
        maze.solve()

        win.wait_for_close()  
        
        cont = input("Want another one? (Y/N) ")
        if cont.lower() == "n":
            print("Closing program, bye bye :)")
            break

if __name__ == "__main__":
    main()