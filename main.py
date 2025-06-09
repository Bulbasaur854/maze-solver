from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    
    line1 = Line(Point(100,300), Point(700,300))
    win.draw_line(line1, "magenta")

    win.wait_for_close()    

if __name__ == "__main__":
    main()