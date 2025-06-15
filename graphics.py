from tkinter import Tk, Frame, Canvas

class Window:
    def __init__(self, board_w, board_h):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.configure(bg="gray10")
        self.__board = Frame(self.__root, bg="gray10")
        self.__board.pack(fill="both", expand=True)
        self.__canvas = Canvas(self.__board, bg="gray10", highlightthickness=0, height=board_h, width=board_w)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)