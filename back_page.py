import tkinter as tk
import sys
def close_window(window):
    window.destroy()


def play_again(window):
    window.destroy()
    sys.exit()
    # Here you can implement logic to restart the game

def show_end_game_screen(time, points, moves):
    # Create a Tkinter window
    end_game_window = tk.Tk()
    end_game_window.title("End of Game")

    # End of game message
    message_label = tk.Label(end_game_window, text="Game Over!")
    message_label.pack(pady=10)

    # Format the time to display only 1 decimal place
    formatted_time = "{:.1f}".format(time)

    # Game information
    info_label = tk.Label(end_game_window, text=f"Time: {formatted_time} seconds\nPoints: {points}\nMoves: {moves}")
    info_label.pack(pady=10)

    # Buttons to close or play again
    close_button = tk.Button(end_game_window, text="Close", command=lambda: close_window(end_game_window))
    close_button.pack(side=tk.LEFT, padx=5)

    # Update window dimensions and position it in the center
    end_game_window.update_idletasks()
    width = end_game_window.winfo_width()
    height = end_game_window.winfo_height()
    x = (end_game_window.winfo_screenwidth() - width) // 2
    y = (end_game_window.winfo_screenheight() - height) // 2
    end_game_window.geometry(f"{width}x{height}+{x}+{y}")

    # Bloquea la ventana hasta que se cierre
    end_game_window.grab_set()

    # Launch the application
    end_game_window.mainloop()


