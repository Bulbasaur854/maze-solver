from tkinter import Button
from graphics import Window
from maze import Maze

def main():
    print("Please enter the dimensions of the maze below (Max = 32x32)")
    COLS = int(input("Columns "))
    ROWS = int(input("Rows "))

    CELL = (COLS + ROWS) // 3
    MARGIN = 24                                 

    board_w = (COLS * CELL) + (MARGIN * 2)
    board_h = (ROWS * CELL) + (MARGIN * 2)
    win  = Window(board_w, board_h)       

    maze = Maze(MARGIN, MARGIN, ROWS, COLS, CELL, CELL, win)
    maze.solve()

    win.wait_for_close()  

if __name__ == "__main__":
    main()