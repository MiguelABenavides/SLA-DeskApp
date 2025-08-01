import tkinter as tk

def create_main_window():

    # the main window instance
    window = tk.Tk()

    # the title of the window
    window.title("The Vaquero Network")

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

    welcome_label.pack(pady=20) # use extra pad to add some vertical space

    # username button
    userName_button = tk.Button(
        window,
        text="Username",
    )
    userName_button.pack(pady=10) # Add some space around the button

    # password button
    password_button = tk.Button(
        window,
        text="Username",
    )
    password_button.pack(pady=10) # Add some space around the button

    # login button widget
    login_button = tk.Button(
        window,
        text="Login",
    )
    login_button.pack(pady=10) # add space around the button

    # return window object to be used in the main file
    return window

