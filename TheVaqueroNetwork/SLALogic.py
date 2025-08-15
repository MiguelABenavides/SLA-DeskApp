# gui.py

import tkinter as tk
from tkinter import messagebox as VaquerosMessager

def on_login_attempt():

    # Get the text entered into the username and password fields
    username = username_entry.get()
    password = password_entry.get()

    # For now, we'll just show what was entered.
    message = f"Attempting login...\nUsername: {username}\nPassword: {password}"
    VaquerosMessager.showinfo("Login Attempt", message)
    print(f"Login attempt - Username: {username}, Password: {password}")

def create_main_window():

    # Create the main window instance.
    window = tk.Tk()

    # Set the title of the window.
    window.title("The Vaquero Network")

    # Set the initial size of the window (width x height).
    window.geometry("400x300")

    # Create a label widget to display a welcome message.
    welcome_label = tk.Label(
        window,
        text="Welcome to The Vaquero Network!",
        font=("Arial", 16)
    )
    welcome_label.pack(pady=20)

    # --- Username Input ---
    username_label = tk.Label(window, text="Username:")
    username_label.pack(pady=(10, 0))

    # Create a global variable for the username entry field
    global username_entry
    username_entry = tk.Entry(window, width=30)
    username_entry.pack(pady=(0, 10))

    # --- Password Input ---
    password_label = tk.Label(window, text="Password:")
    password_label.pack(pady=(10, 0))

    # Create a global variable for the password entry field
    global password_entry
    password_entry = tk.Entry(window, width=30, show="*")
    password_entry.pack(pady=(0, 20))

    # --- Login Button ---
    login_button = tk.Button(
        window,
        text="Login",
        command=on_login_attempt
    )
    login_button.pack(pady=10)

    # Return the window object to be used in the main file.
    return window
