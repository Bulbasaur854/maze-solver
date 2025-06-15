from tkinter import Button
from graphics import Window
from maze import Maze

def main():
    ROWS, COLS = 10, 10
    CELL = 36 
    MARGIN = 24                                 

    board_w = (COLS * CELL) + (MARGIN * 2)
    board_h = (ROWS * CELL) + MARGIN
    win  = Window(board_w, board_h)       

    maze = Maze(MARGIN, MARGIN, ROWS, COLS, CELL, CELL, win)

    btn = Button(win._Window__root, text="SOLVE", font=("Terminal", 10), command=maze.solve)
    btn.pack(pady=MARGIN)

    win.wait_for_close()  

if __name__ == "__main__":
    main()