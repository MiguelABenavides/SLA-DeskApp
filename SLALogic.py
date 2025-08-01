import tkinter as tk

def create_main_window():

    # the main window instance
    window = tk.Tk()

    # the title of the window
    window.title("School Social Life App")

    # the initial size of the window (w x h)
    window.geometry("400x300")

    # create a label widget to display a welcome message
    welcome_label = tk.Label(
        window,
        text="Welcome to the School Social Life App!",
        font=("Arial", 16)
    )

    # the label into the window with padding
    welcome_label.pack(pady=50)

    # return the window object to be used in the main file.
    return window

