import tkinter as tk
import deep_search as ds
import random
targets = [(7,7),(8,9)]
# Definimos la matriz
matrix = [[0] * 20 for _ in range(18)]

# Creamos una ventana
root = tk.Tk()
root.title("Matrix Display")
root.geometry("854x480")  # Establecemos el tamaño de la ventana

# Creamos un canvas
canvas = tk.Canvas(root, width=854, height=480, bg="white")
canvas.pack()

# Inicializamos la matriz y la lista de objetivos
matrix = [[0] * 20 for _ in range(18)]


# Dibujamos la matriz en el canvas
def draw_matrix():
    canvas.delete("all")  # Borra todo lo dibujado en el canvas para evitar superposiciones
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            draw_cell(i, j, "white")


def draw_cell(row, col, selected_color):
    cell_width = 854 / 20
    cell_height = 480 / 18
    
    x0 = col * cell_width
    y0 = row * cell_height
    x1 = x0 + cell_width
    y1 = y0 + cell_height
    color = selected_color if matrix[row][col] == 1 else "white"  # Cambiar color según el valor
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")  # Añade un borde negro a los rectángulos

def place_target(event):
    col = int(event.x / (854 / 20))
    row = int(event.y / (480 / 18))
    coords = (row,col)
    if coords in obstacles or coords in targets:
        return
    if matrix[row][col] == 0:
        matrix[row][col] = 1
        targets.append((row,col))
    else:
        matrix[row][col] = 0
    draw_cell(row,col,"blue")
    print(targets)

snake_positions = []

def place_target_snake(target, selected_color):
    row, col = target
    matrix[row][col] = 1
    snake_positions.append((row, col))
    draw_cell(row, col, selected_color)

def clear_snake():
    for row,col in snake_positions:
        if (row, col) not in obstacles:  # Evitar borrar obstáculos
            matrix[row][col] = 0
            draw_cell(row, col, "white")
    snake_positions.clear()
def move_snake(route, selected_color):
    for target in route:
        clear_snake()
        place_target_snake(target, selected_color)
        root.update()
        root.after(500)
    check_goal_collision()
def generar_coordenadas(num_coordenadas):
    return [(random.randint(0, 17), random.randint(0, 19)) for _ in range(num_coordenadas)]
def print_obstacles():
    for i in obstacles:
        matrix[i[0]][i[1]] = 1
        draw_cell(i[0],i[1],"red")
def generate_route(start,end,obstacles):
    route = list(reversed(ds.prof(start,end,obstacles)))
    print(route)
    return route
def check_goal_collision():
    head = snake_positions[0]  # Obtener la posición de la cabeza de la serpiente
    if head in targets:
        targets.remove(head)  # Eliminar el objetivo alcanzado
        matrix[head[0]][head[1]] = 0  # Actualizar la matriz
        draw_cell(head[0], head[1], "white")  # Borrar el objetivo del canvas
     
        move_snake(generate_route(head,targets[0],obstacles), "green")  # Llamar a move_snake para continuar el movimiento de la serpiente
canvas.bind("<Button-1>", place_target)
obstacles = generar_coordenadas(30)
matrix[7][7] = 1
matrix[8][9] = 1
draw_matrix()
draw_cell(7,7,"blue")
draw_cell(8,9,"blue")
print_obstacles()

move_snake(generate_route((0,0),(7,7),obstacles),"green")
# Ejecutamos la ventana
root.mainloop()

