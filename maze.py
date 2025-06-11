import time
from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                if self.__win:                
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        offset_x = i * self.__cell_size_x
        offset_y = j * self.__cell_size_y
        pos_x1 = self.__x1 + offset_x
        pos_y1 = self.__y1 + offset_y
        pos_x2 = pos_x1 + self.__cell_size_x
        pos_y2 = pos_y1 + self.__cell_size_y
        self.__cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        self.__animate()
        time.sleep(0.01)

    def __animate(self):
        if self.__win:
            self.__win.redraw()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(len(self.__cells)-1, len(self.__cells[0])-1)
