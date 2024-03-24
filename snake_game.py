import tkinter as tk
import time
import deep_search as ds
import random
import tkinter.font as tkFont
import back_page as bp
# Initialize variables
targets = []  # Stores coordinates of targets
matrix = [[0] * 20 for _ in range(18)]  # Matrix representing the game grid
snake_moves = 0  # Number of moves made by the snake
points = 0  # Points collected by the snake
current_routing = []  # Stores the current route for the snake
snake_positions = []  # Stores the positions of the snake's body
game_time = 0  # Elapsed game time
start_time = 0  # Starting time of the game

root = tk.Tk()
root.title("Matrix Display")
root.geometry("1080x720")  # Set window size
root.configure(bg="black")
canvas = tk.Canvas(root, width=854, height=480, bg="#a2a2a2")
canvas.place(x=(1080 - 854) // 2, y=(720 - 480) // 2)  # Center the canvas in the window

def close_window():
    global root
    root.destroy()
    return
def draw_matrix():
    """
    Clears the canvas and draws the game matrix with colored cells.
    """
    canvas.delete("all")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            draw_cell(i, j, "#a2a2a2")


def draw_cell(row, col, selected_color):
    """
    Draws a single cell on the canvas with the specified color.

    Args:
        row (int): Row index of the cell.
        col (int): Column index of the cell.
        selected_color (str): Color to fill the cell with.
    """
    if canvas.winfo_exists():  # Verifica si el canvas todavía existe
        cell_width = 854 / 20
        cell_height = 480 / 18

        x0 = col * cell_width
        y0 = row * cell_height
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        color = selected_color if matrix[row][col] == 1 else "#a2a2a2"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

def place_target(event):
    """
    Places a target on the clicked cell of the canvas.

    Args:
        event (tk.Event): Mouse click event.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    col = int((event.x / canvas_width) * 20)
    row = int((event.y / canvas_height) * 18)

    coords = (row, col)
    if coords in obstacles or coords in targets:
        return

    if not targets:
        matrix[row][col] = 1
        targets.append((row, col))
        draw_cell(row, col, "blue")
        start_game()

    if matrix[row][col] == 0:
        matrix[row][col] = 1
        targets.append((row, col))
    else:
        matrix[row][col] = 0
    draw_cell(row, col, "blue")


def start_game():
    """
    Starts the game by initializing game variables and generating the initial snake route.
    """
    global game_time, start_time, current_routing
    game_time = 0
    start_time = time.time()
    current_routing = generate_route((0, 0), targets[0], obstacles)
    move_snake(current_routing, "green")


def place_target_snake(target, selected_color):
    """
    Places a target on the canvas representing the snake's body.

    Args:
        target (tuple): Coordinates (row, col) of the target.
        selected_color (str): Color to fill the target with.
    """
    row, col = target
    matrix[row][col] = 1
    snake_positions.append((row, col))
    draw_cell(row, col, selected_color)


def clear_snake():
    """
    Clears the snake's body from the canvas.
    """
    for row, col in snake_positions:
        if (row, col) not in obstacles:
            matrix[row][col] = 0
            draw_cell(row, col, "#a2a2a2")
    snake_positions.clear()


def move_snake(route, selected_color):
    """
    Moves the snake along the given route on the canvas.

    Args:
        route (list): List of coordinates representing the route.
        selected_color (str): Color to fill the snake with.
    """
    global game_time, snake_moves
    for target in route:
        clear_snake()
        place_target_snake(target, selected_color)
        root.update()
        root.after(400)
        game_time = time.time() - start_time
        snake_moves += 1
        print_game_time()
        print_snake_moves()
    check_goal_collision()



def generate_coordinates(num_coordinates):
    """
    Generates random coordinates within the game grid.

    Args:
        num_coordinates (int): Number of coordinates to generate.

    Returns:
        list: List of randomly generated coordinates.
    """
    # Generate random coordinates excluding (0, 0) as an obstacle
    coordinates = [(random.randint(0, 17), random.randint(0, 19)) for _ in range(num_coordinates)]
    coordinates = [(x, y) for x, y in coordinates if (x, y) != (0, 0)]
    return coordinates



def print_obstacles():
    """
    Prints the obstacles on the canvas.
    """
    for i in obstacles:
        matrix[i[0]][i[1]] = 1
        draw_cell(i[0], i[1], "red")


def generate_route(start, end, obstacles):
    """
    Generates a route between two points using a pathfinding algorithm.

    Args:
        start (tuple): Starting coordinates (row, col).
        end (tuple): Ending coordinates (row, col).
        obstacles (list): List of obstacle coordinates.

    Returns:
        list: List of coordinates representing the generated route.
    """
    route = list(reversed(ds.depth_first_search(start, end, obstacles)))
    return route


def check_goal_collision():
    """
    Checks for collision between the snake's head and the targets.
    If a collision occurs, updates points and generates a new route for the snake.
    """
    global points, current_routing
    head = snake_positions[0]
    if head in targets:
        points += 1
        targets.remove(head)
        matrix[head[0]][head[1]] = 0
        draw_cell(head[0], head[1], "#a2a2a2")
        print_points()
        if len(targets) == 0:
            close_window()
            bp.show_end_game_screen(game_time,points,snake_moves)
        else:
            current_routing = generate_route(head, targets[0], obstacles)
            move_snake(current_routing, "green")


def print_game_time():
    """
    Prints the elapsed game time on the GUI.
    """
    global game_time
    time_label.config(text="Time: {:.1f} s".format(game_time))


def print_snake_moves():
    """
    Prints the number of moves made by the snake on the GUI.
    """
    moves_label.config(text="Moves: {}".format(snake_moves))


def print_points():
    """
    Prints the total points collected by the snake on the GUI.
    """
    points_label.config(text="Points: {}".format(points))


canvas.bind("<Button-1>", place_target)
draw_matrix()
obstacles = generate_coordinates(30)
print_obstacles()

# Labels for displaying game information
moves_label = tk.Label(root, text="Moves: 0")
moves_label.configure(font=("Arial", 16))

time_label = tk.Label(root, text="Time: 0.0 s")
time_label.configure(font=("Arial", 16)) 

points_label = tk.Label(root, text="Points: 0")
points_label.configure(font=("Arial", 16)) 

time_label.place(x=(1080 - 854) // 2 + 10 - 10, y=(720 - 480) // 2 + 10 - 50) 
font = tkFont.Font(size=16)  
time_label.configure(font=font)

moves_label.place(x=(1080 - 854) // 2 + 10 + 370, y=(720 - 480) // 2 + 10 - 50) 
moves_label.configure(font=font)

points_label.place(x=(1080 - 854) // 2 + 10 + 755, y=(720 - 480) // 2 + 10 - 50) 
points_label.configure(font=font)

root.mainloop()
