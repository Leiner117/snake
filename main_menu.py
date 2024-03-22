import tkinter as tk

def start_game():
    print("Starting game...")  # Aquí puedes agregar la lógica para iniciar el juego

def show_high_scores():
    print("Showing high scores...")  # Aquí puedes agregar la lógica para mostrar las mejores calificaciones

def quit_game():
    root.destroy()  # Cierra la ventana principal

# Crear ventana principal
root = tk.Tk()
root.title("Game")
root.geometry("1280x720")  # Establecer el tamaño de la ventana en 1280x720 píxeles

# Definir estilo retro de arcade
button_style = {"font": ("Courier", 24, "bold"), "bg": "black", "fg": "white", "bd": 3}

# Crear botones con estilo retro de arcade
btn_start_game = tk.Button(root, text="Start Game", command=start_game, **button_style)
btn_start_game.pack(pady=20)

btn_high_scores = tk.Button(root, text="High Scores", command=show_high_scores, **button_style)
btn_high_scores.pack(pady=20)

btn_quit = tk.Button(root, text="Quit", command=quit_game, **button_style)
btn_quit.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
