import time, random
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
            seed=None,
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed:
            random.seed(seed)
        self.__cells = []

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
        time.sleep(0.001)

    def __animate(self):
        if self.__win:
            self.__win.redraw()

    def __draw(self):
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(len(self.__cells)-1, len(self.__cells[0])-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            need_to_visit = []
            
            # determine which cells to visit next
            # left
            if i > 0 and not self.__cells[i-1][j].visited:
                need_to_visit.append((i-1, j))
            # right
            if i < self.__num_cols-1 and not self.__cells[i+1][j].visited:
                need_to_visit.append((i+1, j))
            # top
            if j > 0 and not self.__cells[i][j-1].visited:
                need_to_visit.append((i, j-1))            
            # bottom
            if j < self.__num_rows-1 and not self.__cells[i][j+1].visited:
                need_to_visit.append((i, j+1))

            # no cells to draw
            if len(need_to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            # choose a random direction
            direction_index = random.randrange(len(need_to_visit))
            # get the next cell index to check
            next_index = need_to_visit[direction_index]

            # break walls between current cell and next one
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # top
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            # bottom
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell.visited = False

    # solving recursively using depth-first 
    def __solve_dfs_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True

        # we are at the "end" cell
        if i == self.__num_cols-1 and j == self.__num_rows-1:
            return True
        
        # left
        if (i > 0 and not self.__cells[i][j].has_left_wall and not self.__cells[i-1][j].visited):
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            if self.__solve_dfs_r(i-1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], True)
        # right
        if (i < self.__num_cols-1 and not self.__cells[i][j].has_right_wall and not self.__cells[i+1][j].visited):
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            if self.__solve_dfs_r(i+1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], True)
        # top
        if (j > 0 and not self.__cells[i][j].has_top_wall and not self.__cells[i][j-1].visited):
            self.__cells[i][j].draw_move(self.__cells[i][j-1])
            if self.__solve_dfs_r(i, j-1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j-1], True)
        # bottom
        if (j < self.__num_rows-1 and not self.__cells[i][j].has_bottom_wall and not self.__cells[i][j+1].visited):
            self.__cells[i][j].draw_move(self.__cells[i][j+1])
            if self.__solve_dfs_r(i, j+1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j+1], True)

        return False

    def solve(self, algo):
        match algo:
            case 1:            
                self.__draw()
                return self.__solve_dfs_r(0, 0)
            case _:
                print("Unknown algorithm choice!")