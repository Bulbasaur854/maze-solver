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

        # get user input for maze dimension and solution algorithm
        try:            
            cols , rows = get_dimensions() 
            algo = get_algorithm()            
        except ValueError:
            print("Error: Please enter valid integers.\n")
            continue

        # caculate a proportionate cell size considering number of rows and columns
        cell_width = MAX_CANVAS_WIDTH // cols
        cell_height = MAX_CANVAS_HEIGHT // rows
        cell_size = min(cell_width, cell_height)

        # calculate the board width and height including margin from the window edges
        board_w = (cols * cell_size) + (MARGIN * 2)
        board_h = (rows * cell_size) + (MARGIN * 2)
        win = Window(board_w, board_h)       

        maze = Maze(MARGIN, MARGIN, rows, cols, cell_size, cell_size, win)
        maze.solve(algo)

        win.wait_for_close()  

        # get user input for looping the program
        cont = input("\nGenerate another maze? (Y/N): ")
        if cont.strip().lower() == "n":
            print_closing()
            break

        # print seperation and start again
        print("\n" + "-" * 60)
        is_first_run = False
        
def print_intro():
    print("\n" + "=" * 60)
    print("MAZE GENERATOR & SOLVER - BY BUL8A54UR".center(60))
    print("=" * 60)

def get_dimensions():
    print("\nEnter the dimensions of the maze below.\n(max recommended = 32)")
    cols = int(input("\nColumns: "))
    rows = int(input("Rows: "))
    return cols, rows

def get_algorithm():
    print("""
What algorithm to use for the solution?

    1) Depth First Search

Enter the number of your choice.
""")
    ans = int(input("Choice: "))
    return ans

def print_closing():
    print("\n" + "-" * 60)
    print("Closing program. Thanks for using the Maze Generator!".center(60))
    print("-" * 60 + "\n")

if __name__ == "__main__":
    main()